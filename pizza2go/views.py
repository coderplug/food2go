from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Pizza, PizzaSize, UserShoppingCart, Order
from django.contrib.auth.models import User

class IndexView(generic.ListView):
    template_name = 'pizza2go/index.html'
    context_object_name = 'ordered_pizza_list'

    def get_queryset(self):
        """Return all pizzas alphabetically."""
        return Pizza.objects.order_by('name')

class ShoppingCartView(generic.ListView):
    template_name = 'pizza2go/shopping_cart.html'
    context_object_name = 'ordered_items_list'

    def get_queryset(self):
        """Returns all items alphabetically."""
        return UserShoppingCart.objects.filter(user=self.request.user).order_by("pizza")

def add_to_cart(request):
    size_id = request.POST.get('sizes')
    size = get_object_or_404(PizzaSize, pk=size_id)
    pizza = size.pizza
    user = request.user
    cart = UserShoppingCart(user = user, pizza = pizza, pizza_size = size)
    cart.save()
    return redirect('/pizza2go/')

def remove_from_cart(request, item_id):
    UserShoppingCart.objects.filter(id=item_id).delete()
    return redirect('/pizza2go/shopping_cart/')

class OrderView(generic.ListView):
    template_name = 'pizza2go/orders.html'
    context_object_name = 'order_list'

    def get_queryset(self):
        """Returns all items by active."""
        return Order.objects.filter(user=self.request.user).order_by("active")