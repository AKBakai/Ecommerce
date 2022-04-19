from django.contrib import admin
from django.utils.safestring import mark_safe
from wear.models import Category, SubCategory, Wear

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )   

@admin.register(Wear)
class WearAdmin(admin.ModelAdmin):
    list_display = (
        'subcategory',
        'name',
        'slug',
        'image',
        'description',
        'price',
        'available',
        'created',
        'uploaded',
    )

    read_only = (
        'get_image',
    )

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.image.url} width="100" heigth="110">')

    get_image.short_description = "Image"
