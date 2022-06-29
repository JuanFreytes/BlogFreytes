from django.urls import path
from .views import index, AddCommentView
from . import views

urlpatterns = [
    path("",index,name='index'),
    path('about/',views.about, name='about'),
    path('post_listado/',views.post_listado, name="post_listado"),
    path('crearpost/', views.crearpost, name='crearpost'),
    path('crearpost/<int:pk>',views.PostDetailView.as_view(), name= 'postdetail'),
    path('editarpost/<int:pk>/editar/',views.PostUpdateView.as_view(), name='editarpost'),
    path('borrarpost/<int:pk>/borrar/',views.PostDeleteView.as_view(),name='borrarpost'),
    path('comment/<int:pk>/comment/',AddCommentView.as_view(), name= 'add_comment'),
]  