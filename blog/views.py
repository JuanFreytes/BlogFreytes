from dataclasses import fields
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from .form import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, "blog/index.html")


def crearpost(request):
    if request.method == 'POST':
        form= PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            post = Post(titulo=data['titulo'], subtitulo=data['subtitulo'], cuerpo=data['cuerpo'],
                             fecha_creacion=data['fecha_creacion'], imagen=data['imagen'])
            post.save()
            return redirect('index')
    form = PostForm()
    return render(request, "blog/post_form.html", {'form': form})


def post_listado(request):
    post_listado = Post.objects.all()
    return render(
        request, "blog/post_listado.html",
        {'post_listado': post_listado}
    )
    
def about(request):
    return render(request, "blog/about.html")

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/postdetalles.html'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = '/post_listado'
    fields = ['titulo', 'subtitulo', 'cuerpo','fecha_creacion','imagen']
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/post_listado'

class AddCommentView(DetailView)  :
    model = Comment
    template_name = "add_comment.html"
    fields = "__all__"
