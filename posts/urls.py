
from django.urls import path
from posts.views import  helloview, welcomeview, welcomeuser, homeuser, profileview, \
    postsindex, showpost, deletePost
urlpatterns = [
    path('hello', helloview, name='helloview'),
    path('welcome', welcomeview, name='welcomeview'),
    ## variable part of the urls
    path('welcome/<name>', welcomeuser, name='welcomeuser'),
    path('home/<int:id>', homeuser, name='homeuser'),
    path('profile', profileview, name='profileview'),
    path('index', postsindex, name='posts.index'),
    path('<int:id>',showpost, name='posts.show' ),
    path('<int:id>/delete',deletePost, name='posts.delete' )
]
