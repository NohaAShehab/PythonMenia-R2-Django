from django.shortcuts import render

# Create your views here.


def contactusview(request):
    return render(request, 'contactus/profile.html')