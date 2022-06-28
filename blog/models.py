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
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)