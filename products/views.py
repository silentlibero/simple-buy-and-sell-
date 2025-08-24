from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, ListView, DeleteView
from .forms import ProductForm
from .models import Product
from cart.models import Cart
from accounts.models import Profile
# from .permissions import CanEdit


class AddProductView(View):
    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.uploader = request.user
            product.save()
            return redirect('all-products')
        else:
            return render(request, 'product/create.html', {'form': form})

    def get(self, request):
        form = ProductForm()
        return render(request, 'product/create.html', {'form': form})


class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/update.html'
    success_url = 'all-products'

    def get_object(self, queryset=None):
        return Product.objects.get(uploader=self.request.user)


class AllProductsView(ListView):
    model = Product
    template_name = 'product/list_products.html'


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        cart, created = Cart.objects.get_or_create(user=request.user.profile)
        role = None
        if request.user.is_authenticated:
            try:
                role = request.user.profile.role
            except Profile.DoesNotExist:
                role = None
        return render(request, 'product/detail.html', {'product': product, 'role': role, 'cart': cart})


class DelProductView(DeleteView):
    model = Product
    template_name = 'product/coniform_delete.html'
    success_url = reverse_lazy('all-products')


class AddProductToCart(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        profile = request.user.profile

        cart, created = Cart.objects.get_or_create(user=profile)
        cart.products.add(product)
        cart.save()
        return redirect('all-products')
