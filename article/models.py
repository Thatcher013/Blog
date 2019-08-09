from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    
    YAZILIM = 'Yazılım'
    SIIR = 'Şiir'
    FIKIR = 'Fikir'
    
    
    kategoriler = [
        (YAZILIM, 'Yazılım'),
        (SIIR, 'Şiir'),
        (FIKIR, 'Fikir'),
        
    ]
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar")
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank = True,null = True,verbose_name="Fotoğraf Ekle")
    kategori = models.TextField(choices=kategoriler,verbose_name="Kategori", default = 'Yok')
    viewNumber = models.IntegerField(verbose_name="Görüntülenme", default=0)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar", null = True)
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
