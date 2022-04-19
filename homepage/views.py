from django.shortcuts import render
from wear.models import Category, SubCategory, Wear


def homepage(request):
    wears = Wear.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    context = {
        'wears':wears,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, 'index.html', context)