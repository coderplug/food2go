from django.shortcuts import render
from django.views import generic
from .models import Pizza

class IndexView(generic.ListView):
    template_name = 'pizza2go/index.html'
    context_object_name = 'ordered_pizza_list'

    def get_queryset(self):
        """Return all pizzas alphabetically."""
        return Pizza.objects.order_by('name')