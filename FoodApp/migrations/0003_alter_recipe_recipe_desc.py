# Generated by Django 4.1 on 2023-09-22 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0002_remove_recipe_created_at_remove_recipe_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_desc',
            field=models.CharField(default='sjdfkljsadklf', max_length=1000),
        ),
    ]
