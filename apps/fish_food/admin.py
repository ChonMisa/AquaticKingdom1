from django.contrib import admin

from apps.fish_food.models import FishFood, FishFoodImage


class FfoodImageInline(admin.TabularInline):
    model = FishFoodImage
    extra = 1


@admin.register(FishFoodImage)
class FfoodImageAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(FishFood)
class FishFoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 100
    inlines = [FfoodImageInline]
