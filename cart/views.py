from .models import Cart
from products.models import Product
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404


class CartView(View):
    def get(self, request, pk):
        cart = Cart.objects.get(pk=pk)
        products = cart.products.all()
        return render(request, 'cart/all_cart.html', {'cart': cart, 'products': products})


class DelProductFromCart(View):
    def get(self, request, pk):
        profile = request.user.profile
        cart = get_object_or_404(Cart, user=profile)
        product = get_object_or_404(Product, pk=pk)
        cart.products.remove(product)
        return redirect('all-products')
