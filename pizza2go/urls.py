from django.urls import path

from . import views

app_name = 'pizza2go'
urlpatterns = [
    path('', views.IndexView.as_view(), name='pizza2go-index'),
    path('add_to_cart/', views.add_to_cart, name='pizza2go-add_to_cart'),
]