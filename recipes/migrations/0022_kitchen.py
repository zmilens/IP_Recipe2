# Generated by Django 3.1.5 on 2021-07-06 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0021_delete_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitchen', models.CharField(db_index=True, max_length=40)),
            ],
        ),
    ]
