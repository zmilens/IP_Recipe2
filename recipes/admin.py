from django.contrib import admin
from .models import Recipe, Сategorie, Author, Ingredient, Сategory_product
from import_export.admin import ImportExportModelAdmin

def make_editor(modeladmin, request, queryset):
    queryset.update(level='redactor')
make_editor.short_description = "Make editor"

def make_editor_in_chief(modeladmin, request, queryset):
    queryset.update(level='editor_in_chief')
make_editor_in_chief.short_description = "Make editor-in-chief"

@admin.register(Recipe)
class RecipeAdmin(ImportExportModelAdmin):
    list_display = ('title', 'category', 'description', 'published', 'author')
    list_display_links = ('title', 'category')
    list_filter = ("category", )
    search_fields = ("title__startswith",)
    pass

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'level')
    ordering = ['author']
    actions = [make_editor_in_chief, make_editor]

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'category')
    list_filter = ("category", )
    search_fields = ("ingredient__startswith",)



#admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Сategorie)
admin.site.register(Сategory_product)
admin.site.register(Author, AuthorAdmin)
