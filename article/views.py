from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request, "dashboard.html", context)
@login_required(login_url = "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Makale başarıyla eklendi.")
        return redirect("article:dashboard")

    return render(request, "addarticle.html", {"form" : form})

def detail(request, id):
    #article = Article.objects.filter(id = id).first()

    article = get_object_or_404(Article, id = id)

    comments = article.comments.all()

    return render(request, "detail.html", {"article": article, "comments":comments})
    

@login_required(login_url = "user:login")
def updateArticle(request, id):

    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if article.author == request.user:
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()

            messages.success(request, "Makale başarıyla güncellendi.")
            return redirect("article:dashboard")
    else:
        messages.info(request, "Başkasının makalesini güncellemeye yetkiniz yok.")
        return redirect("article:dashboard")
        


    return render(request, "update.html", {"form":form})
@login_required(login_url = "user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id=id)
    if article.author == request.user:
        article.delete()
        messages.success(request, "Makale Başarıyla Silindi")
        return redirect("article:dashboard")
    else:
        messages.info(request, "Başkasının makalesini silmeye yetkiniz yok.")
        return redirect("article:dashboard")

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request, "articles.html", {"articles":articles})

    articles = Article.objects.all()

    return render(request, "articles.html", {"articles":articles})

@login_required(login_url = "user:login")
def addComment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_content=comment_content)
        newComment.author = request.user
        newComment.article = article
        newComment.save()

    return redirect(reverse("article:detail", kwargs={"id":id}))

@login_required(login_url = "user:login")
def deleteComment(request, id):
    comment = get_object_or_404(Comment, comment_id = id)
    if comment.author == request.user:
        comment.delete()
    article = comment.article
    return redirect(reverse("article:detail", kwargs={"id":article.id}))


    

