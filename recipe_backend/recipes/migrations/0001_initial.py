# Generated by Django 4.1.13 on 2024-10-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=255)),
                ('preparation_time', models.CharField(max_length=100)),
                ('cooking_time', models.CharField(max_length=100)),
                ('total_time', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('cuisine', models.CharField(max_length=100)),
                ('servings', models.IntegerField()),
                ('calories', models.IntegerField(blank=True, null=True)),
                ('preparation_instructions', models.TextField()),
                ('ingredients', models.ManyToManyField(to='recipes.ingredient')),
            ],
        ),
    ]
