from django.contrib import admin

from recipes_list.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'description'
    list_display_links = 'id', 'title'
