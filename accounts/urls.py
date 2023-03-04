from django.urls import path, include

from accounts.views import RegisterUser, ProfileView
urlpatterns=[

    path('',include('django.contrib.auth.urls')),
    path('register',RegisterUser.as_view(),name='account.register' ),
    path('profile/',ProfileView.as_view(), name='accounts.profile')


]