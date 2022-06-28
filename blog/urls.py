from django.urls import path, re_path
from .views import index
from . import views

urlpatterns = [
    path("",index,name='index'),
    path('about/',views.about, name='about'),
    path('post_listado/',views.post_listado, name="post_listado"),
    path('crearpost/', views.crearpost, name='crearpost'),
    path('crearpost/<int:pk>',views.PostDetailView.as_view(), name= 'postdetail'),
    path('editarpost/<int:pk>/editar/',views.PostUpdateView.as_view(), name='editarpost'),
    path('borrarpost/<int:pk>/borrar/',views.PostDeleteView.as_view(),name='borrarpost'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]  