from django.urls import path
from .views import *
from cart.views import *
urlpatterns = [
    path('create/', AddProductView.as_view(), name='create-product'),
    path('<int:pk>/edit/', UpdateProductView.as_view(), name='edit-product'),
    path('<int:pk>/delete/', DelProductView.as_view(), name='del-product'),
    path('all/', AllProductsView.as_view(), name='all-products'),
    path('<int:pk>/detail/', ProductDetail.as_view(), name='detail-product'),
    path('<int:pk>/add-to-cart/', AddProductToCart.as_view(), name='add-to-cart'),
    path('<int:pk>/cart/', CartView.as_view(), name='all-cart'),
    path('<int:pk>/remove-from-cart/', DelProductFromCart.as_view(), name='remove-from-cart')
]
