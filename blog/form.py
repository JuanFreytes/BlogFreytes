from django import forms
from ckeditor.fields import RichTextFormField



class PostForm (forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    cuerpo = RichTextFormField(required=False)
    fecha_creacion = forms.DateTimeField()
    imagen = forms.ImageField()

