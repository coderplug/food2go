from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'pizza2go'
urlpatterns = [
    path('', views.IndexView.as_view(), name='pizza2go-index'),
    path('add_to_cart/', views.add_to_cart, name='pizza2go-add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='pizza2go-remove_from_cart'),
    path('shopping_cart/', views.ShoppingCartView.as_view(), name='pizza2go-shopping_cart'),
    path('orders/', views.OrderView.as_view(), name='pizza2go-orders')
]