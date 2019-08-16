from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('addarticle/', views.addArticle, name = "addarticle"),
    path('article/<int:id>', views.detail, name = "detail"),
    path('update/<int:id>', views.updateArticle, name = "update"),
    path('delete/<int:id>', views.deleteArticle, name = "delete"),
    path('', views.articles, name = "articles"),
    path('comment/<int:id>', views.addComment, name = "comment"),
    path('comment_delete/<int:id>', views.deleteComment, name = "comment_delete"),
    path('yazilim/', views.yazilim, name = "yazilim"),
    path('siir/', views.siir, name = "siir"),
    path('fikir/', views.fikir, name = "fikir"),
    path('ara/', views.ara, name="ara"),
    path('commentOfcomment/<int:id>', views.addCommentofComment, name="commentOfComment"),
    path('comment_re_delete/<int:id>', views.deleteCommentOfComment, name="comment_re_delete")
    
]
