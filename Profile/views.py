from django.shortcuts import render,redirect, get_object_or_404
from .forms import ProfileForm
from .models import Profile, User
from django.contrib import messages

# Create your views here.

def profile(request, name):
    user = get_object_or_404(User, username=name)
    profile = Profile.objects.filter(user=user).first()
    return render(request, "profile.html", {"user":user, "profile":profile})

def profileEdit(request, name):
    user = get_object_or_404(User, username=name)
    profile = Profile.objects.filter(user=user).first()
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if user == request.user:
        if form.is_valid():
        
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "Profil başarıyla güncellendi.")

            return redirect("index")
    else:
        messages.info(request, "Başkasının makalesini güncellemeye yetkiniz yok.")
        return redirect("index")
    context = {
            "form" : form
    }

    return render(request, "profileEdit.html" ,context)

