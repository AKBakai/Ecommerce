from django.shortcuts import render
from .models import Category, SubCategory, Wear


def product(request):
    products = Wear.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, 'product.html', context)


def product_detail(request, slug):
    product_detail = Wear.objects.get(slug=slug)
    context = {
        'product_detail': product_detail,
    }
    return render(request, 'product-detail.html', context)
