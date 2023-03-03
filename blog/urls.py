"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts.views import  helloview, welcomeview, welcomeuser, homeuser, profileview, \
    postsindex, showpost

from contactus.views import contactusview
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello', helloview, name='helloview'),
    # path('welcome', welcomeview, name='welcomeview'),
    # ## variable part of the urls
    # path('welcome/<name>', welcomeuser, name='welcomeuser'),
    # path('home/<int:id>', homeuser, name='homeuser'),
    # path('profile', profileview, name='profileview'),
    path('mmmmmmmm', contactusview, name='contactus'),
    # path('posts/index', postsindex, name='posts.index'),
    # path('posts/<int:id>',showpost, name='posts.show' ),
    path('posts/', include('posts.urls'))
    ##generate url for your media files
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
