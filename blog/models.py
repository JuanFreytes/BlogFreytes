from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.

class Post (models.Model):
    titulo= models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    cuerpo = RichTextField(null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to= 'blogimagen',null=True)

    def __str__(self):
        return f'{self.titulo} {self.subtitulo}'

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text