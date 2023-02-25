from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### any view must return with HTTP Response
def helloview(request):
    return HttpResponse("Hello world")


def welcomeview(request):
    return HttpResponse("<h1 style='color:red; text-align:center'> Welcome to django </h1>")

def welcomeuser(request, name):
    return HttpResponse(f"<h1 style='color:red; text-align:center'> Welcome {name} </h1>")


def homeuser(request, id):
    return HttpResponse(f"<h1 style='color:red; text-align:center'> {id} </h1>")


def profileview(request):
    message = 'Nice to you meet you'

    users = [
        "Rowida", 'AbdAllah', 'Dina', 'Michael', 'Yossef', 'Yossef', 'Osama'
    ]

    return render(request, 'posts/profile.html', context={'mymessage':message, 'users':users})



posts = [
        {"id":1, "title":"post1", "description":"post1 description"},
        {"id": 2, "title": "post2", "description": "post2 description"},
        {"id": 3, "title": "post3", "description": "post3 description"},
    ]

def postsindex(request):
    return  render(request, 'posts/index.html', context={"posts":posts})



def showpost(request,id):
    print(type(id))
    for post in posts:
        if post['id']==id:
            return render(request, 'posts/show.html', context={"post":post})
    else:
        return HttpResponse("Post Not Found")






