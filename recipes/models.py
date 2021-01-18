from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Сategorie', null=True, on_delete= models.PROTECT)
    description = models.TextField(null=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    author = models.ForeignKey('Author', null=True, on_delete=models.PROTECT)

    class Meta:
        db_table = "web_recipe"


    def __str__(self):
        return self.title


class Сategorie(models.Model):
    category = models.CharField(max_length=40, db_index=True)
    def __str__(self):
        return self.category


class Сategory_product(models.Model):
    category_product = models.CharField(max_length=40, db_index=True)
    def __str__(self):
        return self.category_product

class Ingredient(models.Model):
    ingredient = models.CharField(max_length=40, db_index=True)
    category = models.ForeignKey('Сategory_product', null=True, on_delete=models.PROTECT)
    def __str__(self):
        return self.ingredient

class Author(models.Model):
    author = models.CharField (max_length=40, db_index=True)
    level = models.CharField(max_length=20)
    def __str__(self):
        return self.author


