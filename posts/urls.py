
from django.urls import path
from posts.views import  helloview, welcomeview, welcomeuser, homeuser, profileview, \
    postsindex, showpost, deletePost, createPost, editpost
urlpatterns = [
    path('hello', helloview, name='helloview'),
    path('welcome', welcomeview, name='welcomeview'),
    ## variable part of the urls
    path('welcome/<name>', welcomeuser, name='welcomeuser'),
    path('home/<int:id>', homeuser, name='homeuser'),
    path('profile', profileview, name='profileview'),
    path('index', postsindex, name='posts.index'),
    path('<int:id>',showpost, name='posts.show' ),
    path('<int:id>/delete',deletePost, name='posts.delete' ),
    path('create', createPost, name='posts.create'),
    path('<int:id>/edit',editpost, name='posts.edit' )
]
