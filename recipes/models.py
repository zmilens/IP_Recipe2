from django.db import models

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    kitchen = models.CharField(max_length=100)
    ingredients = models.TextField(null=True)
    description = models.TextField(null=True)
    published = models.DateField(auto_now_add=True, db_index=True)
    author = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Сategorie(models.Model):
    category = models.CharField(max_length=40, db_index=True)
    def __str__(self):
        return self.category


class Kitchen(models.Model):
    kitchen = models.CharField(max_length=40, db_index=True)
    def __str__(self):
        return self.kitchen


class Authors(models.Model):
    authorId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    def __str__(self):
        return self.name



