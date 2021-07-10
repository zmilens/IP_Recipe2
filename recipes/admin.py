from django.contrib import admin
from .models import Сategorie, Authors, Kitchen, Recipe
from import_export.admin import ImportExportModelAdmin


@admin.register(Recipe)
class RecipeAdmin(ImportExportModelAdmin):
    list_display = ('title', 'category', 'kitchen', 'ingredients', 'description', 'published', 'author')
    list_display_links = ('title', 'category')
    list_filter = ("category", )
    search_fields = ("title__startswith",)
    pass

@admin.register(Authors)
class AuthorsAdmin(ImportExportModelAdmin):
    list_display = ('name', 'surname')
    ordering = ['name']
    pass


@admin.register(Kitchen)
class KitchenAdmin(ImportExportModelAdmin):
    list_display = ('kitchen', )

@admin.register(Сategorie)
class СategorieAdmin(ImportExportModelAdmin):
    list_display = ('category',)
