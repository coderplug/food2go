from django.test import TestCase
from .models import Pizza, PizzaSize, Topping
from decimal import Decimal
from django.core.exceptions import ValidationError

class PizzaSizeTests(TestCase):
    def test_is_created_with_negative_diameter(self):
        """
        Pizza with negative diameter -1 is not created
        """
        topping = Topping(name="Cheese")
        topping.save()
        pizza = Pizza(name="Cheese Pizza")
        pizza.save()
        pizza.toppings.add(topping)
        pizza_size = PizzaSize(
            name="Extra negative", 
            diameter=-1,
            pizza = pizza,
            price = Decimal(10))
        with self.assertRaises(ValidationError):
            #full_clean called to check MinValueValidator, MaxValueValidator
            #   Called explicitly to not cause issues in forms
            #Another solution: use a ModelForm
            pizza_size.full_clean() 
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError
        #self.assertIs(pizza_size.pk, None)

    def test_is_created_with_zero_diameter(self):
        """
        Pizza with diameter 0 is not created
        """
        topping = Topping(name="Cheese")
        topping.save()
        pizza = Pizza(name="Cheese Pizza")
        pizza.save()
        pizza.toppings.add(topping)
        pizza_size = PizzaSize(
            name="Empty space", 
            diameter=0,
            pizza = pizza,
            price = Decimal(10))
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError

    def test_is_created_with_minimum_diameter(self):
        """
        Pizza with minimum diameter 1 is created
        """
        topping = Topping(name="Cheese")
        topping.save()
        pizza = Pizza(name="Cheese Pizza")
        pizza.save()
        pizza.toppings.add(topping)
        pizza_size = PizzaSize(
            name="Extra Small",
            diameter=1,
            pizza=pizza,
            price= Decimal(10))
        pizza_size.full_clean()
        pizza_size.save()
        self.assertTrue(pizza_size.pk, not None)

    def test_is_created_with_maximum_diameter(self):
        """
        Pizza with maximum diameter 100 is created
        """
        pizza = Pizza(name="Cheese Pizza")
        pizza.save()
        pizza.toppings.create(name="Cheese")
        pizza_size = PizzaSize(
            name="Extra Large", 
            diameter=100,
            pizza = pizza,
            price = Decimal(10))
        pizza_size.full_clean()
        pizza_size.save()
        self.assertTrue(pizza_size.pk, not None)

    def test_is_created_with_over_maximum_diameter(self):
        """
        Pizza with maximum diameter 101 is not created
        """
        topping = Topping(name="Cheese")
        topping.save()
        pizza = Pizza(name="Cheese Pizza")
        pizza.save()
        pizza.toppings.add(topping)
        pizza_size = PizzaSize(
            name="Too Extra Large", 
            diameter=101,
            pizza = pizza,
            price = Decimal(10))
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError
    