# Generated by Django 3.1.5 on 2021-01-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_delete_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='level',
            field=models.CharField(default=2, max_length=1),
            preserve_default=False,
        ),
    ]
