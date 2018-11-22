from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class Topping(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length = 30)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name

class PizzaSize(models.Model):
    name = models.CharField(max_length = 30)
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
    def __str__(self):
        return self.name