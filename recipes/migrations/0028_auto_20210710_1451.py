# Generated by Django 3.1.5 on 2021-07-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0027_auto_20210710_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='kitchen',
            field=models.CharField(default=5, max_length=100),
            preserve_default=False,
        ),
    ]