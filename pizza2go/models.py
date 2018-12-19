from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Topping(models.Model):
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(unique=True, max_length=30)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name

class PizzaSize(models.Model):
    name = models.CharField(max_length=30)
    diameter = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
    ])
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    #price = models.OneToOneField('PizzaPrice', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=2, validators=[
        MaxValueValidator(Decimal("99.99")),
        MinValueValidator(Decimal("0.01"))
    ])

    class Meta:
        ordering = ['diameter']
        unique_together = ('name', 'pizza',)

    def __str__(self):
        return self.name

class UserShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    pizza_size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)

    def __str__(self):
        username = self.user.username
        pizza_size_name = self.pizza_size.name
        pizza_name = self.pizza.name
        result = "%s: %s %s pizza" % (username, pizza_size_name, pizza_name)
        return result

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)
    date_finished = models.DateField(null=True, blank=True)
    time_finished = models.TimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def get_price(self):
        order_sum = Decimal(0.0)
        order_items = self.orderitem_set.all()
        for item in order_items:
            order_sum += item.pizza_size.price
        return order_sum

    def __str__(self):
        username = self.user.username
        active = "active" if self.active else "inactive"
        result = "%s's %s order, created at %s" % (username, active, self.date_created)
        return result

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    pizza_size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)

    def __str__(self):
        order = self.order
        pizza_size_name = self.pizza_size.name
        pizza_name = self.pizza.name
        result = "%s order - %s %s pizza" % (order, pizza_size_name, pizza_name)
        return result
