# Generated by Django 5.0.4 on 2024-07-21 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0003_rename_accessory_accessoryimage_accessory_ac_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessory',
            name='image',
        ),
    ]
