# Generated by Django 5.0.4 on 2024-06-11 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_rename_title_fishcategory_name'),
        ('fish', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fishes', to='categories.fishcategory', verbose_name='Категории рыб'),
        ),
    ]
