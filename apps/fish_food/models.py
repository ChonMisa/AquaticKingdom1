import os

from django.db import models

from utils.image_path import fish_food_images


class FishFood(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    stock = models.PositiveIntegerField(
        default=0,
    )
    restock_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
    )
    # image = models.ImageField(
    #     upload_to=fish_food_images,
    #     verbose_name="Изображение",
    #     blank=True,
    #     null=True
    # )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Slug"
    )

    def __str__(self):
        return self.title


class FishFoodImage(models.Model):
    ffoodd = models.ForeignKey(
        FishFood,
        on_delete=models.CASCADE,
        related_name='ffood_images',
        verbose_name="Корм для рыбы"
    )
    image = models.ImageField(
        upload_to=fish_food_images,
        verbose_name="Картинка корма"
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.image.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return f'{self.ffoodd.title}'

    class Meta:
        verbose_name = "Изображение корма рыб"
        verbose_name_plural = "Изображение корма рыбы"
