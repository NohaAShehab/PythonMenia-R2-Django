

# path('', Home.as_view(), name='home')

from django.urls import path

from categories.views import AllCategories, CreateCategory, \
    CategoryListView,CategoryCreateView, CategoryDetailedView, \
    CategoryUpdateView,CategoryDeleteView
urlpatterns = [
    # path('', AllCategories.as_view(), name='categories.index'),
    # path('create',CreateCategory.as_view(), name='categories.create' ),
    ### generic views
    path('', CategoryListView.as_view(), name='categories.index'),
    path('create',CategoryCreateView.as_view(), name='categories.create' ),
    path('<int:pk>', CategoryDetailedView.as_view(), name='categories.show'),
    path('<int:pk>/edit', CategoryUpdateView.as_view(), name='categories.edit'),
    path('<int:pk>/delete', CategoryDeleteView.as_view(), name='categories.delete')

]