from import_export import resources
from recipes.models import Recipe


class RecipeResource(resources.ModelResource):

    class Meta:
        model = Recipe