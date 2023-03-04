from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from posts.models import Post
from categories.models import Category
from posts.forms import PostForm, PostModelForm
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



# posts = [
#         {"id":1, "title":"post1", "description":"post1 description", 'image': 'pic2.png'},
#         {"id": 2, "title": "post2", "description": "post2 description", 'image': 'pic3.png' },
#         {"id": 3, "title": "post3", "description": "post3 description",  'image': 'pic4.png'},
#     ]

def postsindex(request):
    posts = Post.get_all_posts()
    return  render(request, 'posts/index.html', context={"posts":posts})



def showpost(request,id):
    # post = Post.objects.get(id=id)
    # post = get_object_or_404(Post, pk=id)
    post = Post.get_spefic_post(id)

    return render(request, 'posts/show.html', context={"post":post})


def deletePost(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, pk=id)
    post.delete()
    # return render(request, 'posts/show.html', context={"post": post})
    # return HttpResponse("post deleted")
    return redirect('posts.index')



def createPost(request):
    print(request)
    if request.method=='GET':
        # postform = PostForm()
        postform = PostModelForm()
        # cats = Category.get_all_categories()
        return render(request, 'posts/createform.html', context={'form': postform})

    elif request.method=='POST':
        postform  = PostModelForm(request.POST, request.FILES)
        if postform.is_valid():
            postform.save()
            return redirect('posts.index')

        # return HttpResponse('post request method')
        return redirect('posts.create')

@login_required()
def editpost(request, id ):
    post = Post.get_spefic_post(id)
    if request.method=='GET':
        postform = PostModelForm(instance=post)
        return render(request, 'posts/editform.html', context={'form': postform})
    if request.method=='POST':
        postform = PostModelForm( request.POST, request.FILES, instance=post)
        if postform.is_valid():
            postform.save()
            return redirect(post.get_show_url())


        return redirect('posts.create')


