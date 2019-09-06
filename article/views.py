from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment,CommentOfComment
from django.contrib.auth.decorators import login_required
import time


# Create your views here.


def index(request):
    articles = Article.objects.all()[:5]
    
    return render(request, "index.html", {"articles":articles})

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
    comment_re = CommentOfComment.objects.filter(article=article)

    time.sleep(2)
    article.viewNumber += 1
    article.save()
    return render(request, "detail.html", {"article": article, "comments":comments, "comments_re":comment_re})
    
    

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
        dogrulamaComment = Comment.objects.filter(author = request.user, article = article, comment_content = comment_content)

        if dogrulamaComment:
            messages.info(request, "Tekrarlanan yorum tespit edildi")
            return redirect(reverse("article:detail", kwargs={"id":id}))
        else:
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
    messages.info(request, "Bro...")
    return redirect(reverse("article:detail", kwargs={"id":article.id}))

def yazilim(request):
    articles = Article.objects.filter(kategori = 'Yazılım')
    if articles:
        return render(request, "articles.html", {"articles":articles})
    messages.info(request, "Maalesef bu kategoride bir yazı bulunmuyor.")
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles":articles})
    
    

def siir(request):
    articles = Article.objects.filter(kategori = 'Şiir')
    if articles:
        return render(request, "articles.html", {"articles":articles})
    
    messages.info(request, "Maalesef bu kategoride bir yazı bulunmuyor.")
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles":articles})

def fikir(request):
    articles = Article.objects.filter(kategori = 'Fikir')
    if articles:
        return render(request, "articles.html", {"articles":articles})
    messages.info(request, "Maalesef bu kategoride bir yazı bulunmuyor.")    
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles":articles})

def teknoloji(request):
    articles = Article.objects.filter(kategori = 'Teknoloji')
    if articles:
        return render(request, "articles.html", {"articles":articles})
    
    messages.info(request, "Maalesef bu kategoride bir yazı bulunmuyor.")
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles":articles})

def oyku(request):
    articles = Article.objects.filter(kategori = 'Öykü')
    if articles:
        return render(request, "articles.html", {"articles":articles})
    
    messages.info(request, "Maalesef bu kategoride bir yazı bulunmuyor.")
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles":articles})

def bilim(request):
    articles = Article.objects.filter(kategori = 'Bilim')
    if articles:
        return render(request, "articles.html", {"articles":articles})
    
    messages.info(request, "Maalesef bu kategoride bir yazı bulunmuyor.")
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles":articles})

def egitim(request):
    articles = Article.objects.filter(kategori = 'Eğitim')
    if articles:
        return render(request, "articles.html", {"articles":articles})
    
    messages.info(request, "Maalesef bu kategoride bir yazı bulunmuyor.")
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles":articles})




def ara(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request, "articles.html", {"articles":articles})

    articles = Article.objects.all()

    return render(request, "articles.html", {"articles":articles})

@login_required(login_url = "user:login")
def addCommentofComment(request, id):
    comment = get_object_or_404(Comment, comment_id=id)
    article = comment.article
    if request.method == "POST":

        comment_content = request.POST.get("comment_re_content")
        dogrulamaComment = CommentOfComment.objects.filter(author = request.user, comment = comment, commentOfComment_content = comment_content)
        
        if dogrulamaComment:
            messages.info(request, "Tekrarlanan cevap tespit edildi")
            return redirect(reverse("article:detail", kwargs={"id":comment.article.id}))
        else:
            newCommentRe = CommentOfComment(commentOfComment_content=comment_content)
            newCommentRe.author = request.user
            newCommentRe.comment = comment
            newCommentRe.article = article
            newCommentRe.save()
    return redirect(reverse("article:detail", kwargs={"id":comment.article.id}))


login_required(login_url="user:login")
def deleteCommentOfComment(request, id):
    comment_re = get_object_or_404(CommentOfComment, commentOfComment_id=id)
    if comment_re.author == request.user:
        comment_re.delete()
        messages.success(request, "Yorum Başarıyla Silindi")
        return redirect(reverse("article:detail", kwargs={"id":comment_re.comment.article.id}))
    else:
        messages.info(request, "Başkasının yorumunu silmeye yetkiniz yok.")
        return redirect(reverse("article:detail", kwargs={"id":comment_re.comment.article.id}))



    



    

