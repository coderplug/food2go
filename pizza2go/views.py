from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Pizza, PizzaSize, UserShoppingCart
from django.contrib.auth.models import User

class IndexView(generic.ListView):
    template_name = 'pizza2go/index.html'
    context_object_name = 'ordered_pizza_list'

    def get_queryset(self):
        """Return all pizzas alphabetically."""
        return Pizza.objects.order_by('name')

def add_to_cart(request):
    print("Worked!")
    size_id = request.POST.get('sizes')
    size = get_object_or_404(PizzaSize, pk=size_id)
    pizza = size.pizza
    user = request.user
    cart = UserShoppingCart(user = user, pizza = pizza, pizza_size = size)
    cart.save()
    print(size_id, size, pizza, user)
    return redirect('/pizza2go/')