from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Recipe


def index_view(request: HttpRequest) -> HttpResponse:
    all_items = Recipe.objects.order_by("time_for_cooking").all()[:2]
    return render(
        request,
        template_name="recipes_list/index.html",
        context={"all_items": all_items},
    )


class RecipeListIndexView(ListView):
    template_name = "recipes_list/index.html"
    queryset = Recipe.objects.order_by("time_for_cooking").all()[:2]

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["all_items"] = Recipe.objects.order_by("time_for_cooking").all()
    #     return {"all_items": context}


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes_list/index.html"
    context_object_name = "all_items"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes_list/index.html"
    context_object_name = "all_items"
