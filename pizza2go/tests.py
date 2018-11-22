from django.test import TestCase
from .models import Pizza, PizzaSize, Topping
from decimal import Decimal
from django.core.exceptions import ValidationError

class PizzaSizeTests(TestCase):
    #For every test
    def setUp(self):
        topping = Topping(name="Cheese")
        topping.save()
        self.pizza = Pizza(name="Cheese Pizza")
        self.pizza.save()
        self.pizza.toppings.add(topping)     
        
    def test_is_created_with_negative_diameter(self):
        """
        Pizza size with negative diameter -1 is not created
        """
        pizza_size = PizzaSize(
            name="Extra negative",
            diameter=-1,
            pizza = self.pizza,
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
        Pizza size with diameter 0 is not created
        """
        pizza_size = PizzaSize(
            name="Empty space", 
            diameter=0,
            pizza = self.pizza,
            price = Decimal(10))
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError

    def test_is_created_with_minimum_diameter(self):
        """
        Pizza size with minimum diameter 1 is created
        """
        pizza_size = PizzaSize(
            name="Extra Small",
            diameter=1,
            pizza = self.pizza,
            price= Decimal(10))
        pizza_size.full_clean()
        pizza_size.save()
        self.assertTrue(pizza_size.pk, not None)

    def test_is_created_with_maximum_diameter(self):
        """
        Pizza size with maximum diameter 100 is created
        """
        pizza_size = PizzaSize(
            name="Extra Large", 
            diameter=100,
            pizza = self.pizza,
            price = Decimal(10))
        pizza_size.full_clean()
        pizza_size.save()
        self.assertTrue(pizza_size.pk, not None)

    def test_is_created_with_over_maximum_diameter(self):
        """
        Pizza size with maximum diameter 101 is not created
        """
        pizza_size = PizzaSize(
            name="Too Much Extra", 
            diameter=101,
            pizza = self.pizza,
            price = Decimal(10))
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError
    
    def test_is_created_with_negative_price(self):
        """
        Pizza size with negative price -0.01 is not created
        """
        pizza_size = PizzaSize(
            name="Debt", 
            diameter=10,
            pizza = self.pizza,
            price = Decimal("-0.01"))
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError

    def test_is_created_with_zero_price(self):
        """
        Pizza size with price 0 is not created
        """
        pizza_size = PizzaSize(
            name="Free", 
            diameter=10,
            pizza = self.pizza,
            price = Decimal("0"))
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError

    def test_is_created_with_too_small_price(self):
        """
        Pizza size with price 0.001 is not created
        """
        pizza_size = PizzaSize(
            name="Too low price", 
            diameter=10,
            pizza = self.pizza,
            price = Decimal("0.001"))
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError

    def test_is_created_with_too_many_decimal_numbers(self):
        """
        Pizza size with price 1.001 is not created
        """
        pizza_size = PizzaSize(
            name="Invalid price", 
            diameter=10,
            pizza = self.pizza,
            price = Decimal("1.001"))
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError

    def test_is_created_with_minimum_price(self):
        """
        Pizza size with minimum price 0.01 is created
        """
        pizza_size = PizzaSize(
            name="Cheapest", 
            diameter=10,
            pizza = self.pizza,
            price = Decimal("0.01"))
        pizza_size.full_clean()
        pizza_size.save()
        self.assertTrue(pizza_size.pk, not None)

    def test_is_created_with_maximum_price(self):
        """
        Pizza size with maximum price 99.99 is created
        """
        pizza_size = PizzaSize(
            name="Most expensive", 
            diameter=10,
            pizza = self.pizza,
            price = Decimal("99.99"))
        pizza_size.full_clean()
        pizza_size.save()
        self.assertTrue(pizza_size.pk, not None)

    def test_is_created_with_too_expensive_price(self):
        """
        Pizza size with too expensive price 100 is not created
        """
        pizza_size = PizzaSize(
            name="Too expensive", 
            diameter=10,
            pizza = self.pizza,
            price = Decimal("100"))
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError
    
    def test_is_created_with_empty_name(self):
        """
        Pizza size with empty name is not created
        """
        pizza_size = PizzaSize(
            name="", 
            diameter=10,
            pizza = self.pizza,
            price = Decimal("100"))
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError
    
    def test_is_created_with_no_name(self):
        """
        Pizza size with no name is not created
        """
        pizza_size = PizzaSize(
            diameter=10,
            pizza = self.pizza,
            price = Decimal("100"))
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError

    def test_is_created_with_no_diameter(self):
        """
        Pizza size with no diameter is not created
        """
        pizza_size = PizzaSize(
            name="Invisible",
            pizza = self.pizza,
            price = Decimal("100"))
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError

    def test_is_created_with_no_price(self):
        """
        Pizza size with no price is not created
        """
        pizza_size = PizzaSize(
            name="No-price",
            diameter=10,
            pizza = self.pizza)
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError

    def test_is_created_with_no_pizza(self):
        """
        Pizza size with no pizza is not created
        """
        pizza_size = PizzaSize(
            name="No-pizza",
            diameter=10,
            price = Decimal("100"))
        with self.assertRaises(ValidationError):
            pizza_size.full_clean()
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError