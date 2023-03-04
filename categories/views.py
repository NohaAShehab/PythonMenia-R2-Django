from django.shortcuts import render, redirect
from django.views import View

from django.views.generic import  ListView, DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView

from categories.models import  Category
from categories.forms import  CategoryModelForm


# Create your views here.
## class based views


### list --> all categories

class AllCategories(View):
    ## get
    def get(self, request):
        categories = Category.get_all_categories()
        return render(request, 'categories/index.html', context={'categories':categories})


class CreateCategory(View):
    def get(self, request):
        categoryform = CategoryModelForm()
        return render(request, 'categories/create.html', context={"form":categoryform})

    def post(self, request):
        categoryform = CategoryModelForm(request.POST, request.FILES)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('categories.index')

        return redirect('categories.create')


################# Generic views

## list all objects
class CategoryListView(ListView):
    model = Category
    template_name = 'categories/index.html'
    # object_list---> use it in the template


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories/create.html'
    form_class = CategoryModelForm
    success_url = '/categories/'


class CategoryDetailedView(DetailView):
    model = Category
    template_name = 'categories/show.html'


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'categories/edit.html'
    form_class = CategoryModelForm
    success_url = '/categories/'


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/delete.html'
    success_url = '/categories/'


