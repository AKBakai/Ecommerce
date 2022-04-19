from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from wear.models import Wear
from .models import Cart
from .forms import CartAddProductForm


def cart(request):
    a = Cart.objects.all()
    product = get_object_or_404(Wear)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        Cart.objects.create(product=product,
                 quantity=cd['quantity'],
                 price = cd['price'],
                 update_quantity=cd['update'])
    return render(request, 'cart.html', {'cart': a})



def update_f_price(request):
    amount = request.POST['amount']
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        form.save()
        Cart.objects.create(amount=amount)
        return redirect('cart')
    return render(request, 'cart.html', {'amount': amount})


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Wear, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

