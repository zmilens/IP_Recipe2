# Generated by Django 3.1.5 on 2021-07-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0026_auto_20210707_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
