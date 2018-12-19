from datetime import datetime
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.models import User

from .models import Pizza, PizzaSize, UserShoppingCart, Order, OrderItem

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
    cart = UserShoppingCart(user=user, pizza=pizza, pizza_size=size)
    cart.save()
    return redirect('/pizza2go/')

def remove_from_cart(request, item_id):
    UserShoppingCart.objects.filter(id=item_id).delete()
    return redirect('/pizza2go/shopping_cart/')

def create_order(request):
    username = request.user
    shopping_cart_items = UserShoppingCart.objects.filter(user=username)
    #TODO: used to avoid ("back -> Create order" empty order). Check if possible to avoid it.
    if not shopping_cart_items:
        order = Order(user=username)
        order.save()
        for item in shopping_cart_items:
            order_item = OrderItem(order=order, pizza=item.pizza, pizza_size=item.pizza_size)
            order_item.save()
        shopping_cart_items.delete()
    return redirect('/pizza2go/orders/')

def complete_order(request, order_id):
    order = get_object_or_404(Order, order_id)
    now = datetime.now()
    order.date_finished = now
    order.time_finished = now
    order.active = False
    order.save()
    return redirect('/pizza2go/orders/')

class OrderView(generic.ListView):
    template_name = 'pizza2go/orders.html'
    context_object_name = 'order_list'

    def get_queryset(self):
        """Returns all items by active."""
        return Order.objects.filter(user=self.request.user).order_by("-active")
