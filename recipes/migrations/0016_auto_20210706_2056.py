# Generated by Django 3.1.5 on 2021-07-06 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_auto_20210706_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='author',
            new_name='authors',
        ),
    ]
