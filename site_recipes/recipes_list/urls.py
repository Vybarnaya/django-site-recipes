from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "recipes_list"

urlpatterns = [
    # path('', views.index_view, name='index'),
    path('', views.RecipeListIndexView.as_view(), name='index'),
    path('list/', views.RecipeListView.as_view(), name='list'),
    path('<int:pk>/', views.RecipeDetailView.as_view(), name='detail'),
]
