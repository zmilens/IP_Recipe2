# Generated by Django 3.1.5 on 2021-07-06 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0025_auto_20210707_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='published',
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
    ]
