# Generated by Django 4.1 on 2023-09-27 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0006_alter_recipe_recipe_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_desc',
            field=models.CharField(default='Recipe detail', max_length=1000),
        ),
    ]