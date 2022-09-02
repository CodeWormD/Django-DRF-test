from django.contrib import admin

from .models import Food, FoodCategory

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name_ru',
        'category',
        'cost',
        'is_publish',
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name_ru',
        'order_id',
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'