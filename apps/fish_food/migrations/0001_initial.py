import utils.image_path
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FishFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('stock', models.PositiveIntegerField(default=0)),
                ('restock_date', models.DateTimeField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to=utils.image_path.fish_food_images, verbose_name='Изображение')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
            ],
        ),
    ]
