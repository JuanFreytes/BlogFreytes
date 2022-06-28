from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post, Comment
from .form import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


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
    

class PostView(DetailView):
    model = Post
    template_name = "core/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        slug = self.kwargs["slug"]

        form = CommentForm()
        post = get_object_or_404(Post, pk=pk, slug=slug)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            comment = Comment.objects.create(
                name=name, email=email, content=content, post=post
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('postdetail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})