from django.test import TestCase
from .models import Pizza, PizzaSize, Topping
from decimal import Decimal
from django.core.exceptions import ValidationError

class ToppingTests(TestCase):
    def test_is_created_working_case(self):
        """
        Topping with proper values is created
        """
        topping = Topping(name="Pickles")
        #full_clean called to check validations (MinValueValidator, MaxValueValidator)
        #   Called explicitly to not cause issues in forms
        #Another solution: use a ModelForm
        topping.full_clean()
        topping.save()
        self.assertTrue(topping.pk, not None)

    def test_is_created_duplicate_case(self):
        """
        Duplicate topping is not created
        """
        topping = Topping(name="Sour cream")
        topping.full_clean()
        topping.save()
        topping = Topping(name="Sour cream")
        with self.assertRaises(ValidationError):
            topping.full_clean()
            topping.save()
            if topping.pk is None:
                raise ValidationError

    def test_is_created_with_empty_name(self):
        """
        Topping without name is not created
        """
        topping = Topping()
        with self.assertRaises(ValidationError):
            topping.full_clean()
            topping.save()
            if topping.pk is None:
                raise ValidationError

    def test_is_created_with_no_name(self):
        """
        Topping with empty name is not created
        """
        topping = Topping(name="")
        with self.assertRaises(ValidationError):
            topping.full_clean()
            topping.save()
            if topping.pk is None:
                raise ValidationError

class PizzaTests(TestCase):
    #For every test (only setUp)
    def setUp(self):
        self.topping = Topping(name="Pineapple")
        self.topping.save()

    def test_is_created_working_case(self):
        """
        Pizza with proper values is created
        """
        pizza = Pizza(name="Hawaii pizza")
        #full_clean called to check validations (MinValueValidator, MaxValueValidator)
        #   Called explicitly to not cause issues in forms
        #Another solution: use a ModelForm
        pizza.full_clean()
        pizza.save()
        pizza.toppings.add(self.topping)
        self.assertTrue(pizza.pk, not None)

    def test_is_created_duplicate_name_case(self):
        """
        Pizza with duplicate name is not created
        """
        pizza = Pizza(name="Hawaii pizza")
        pizza.full_clean()
        pizza.save()
        pizza = Pizza(name="Hawaii pizza")
        with self.assertRaises(ValidationError):
            pizza.full_clean()
            pizza.save()
            if pizza.pk is None:
                raise ValidationError
            

    def test_is_created_with_no_topping(self):
        """
        Pizza without topping is created
        """
        pizza = Pizza(name="Hawaii pizza")
        pizza.full_clean()
        pizza.save()
        self.assertTrue(pizza.pk, not None)

    def test_is_created_with_empty_name(self):
        """
        Pizza without name is not created
        """
        pizza = Pizza(name="")
    
        with self.assertRaises(ValidationError):
            pizza.full_clean()
            pizza.save()
            if pizza.pk is None:
                raise ValidationError

    def test_is_created_with_no_name(self):
        """
        Pizza without name is not created
        """
        pizza = Pizza()
    
        with self.assertRaises(ValidationError):
            pizza.full_clean()
            pizza.save()
            if pizza.pk is None:
                raise ValidationError

class PizzaSizeTests(TestCase):
    #For every test (only setUp)
    def setUp(self):
        topping = Topping(name="Cheese")
        topping.save()
        self.pizza = Pizza(name="Cheese Pizza")
        self.pizza.save()
        self.pizza.toppings.add(topping)     

    def test_is_created_working_case(self):
        """
        Pizza size with working values is created
        """
        pizza_size = PizzaSize(
            name="Normal",
            diameter = 30,
            pizza = self.pizza,
            price = Decimal(7))
        pizza_size.full_clean()
        pizza_size.save()
        self.assertTrue(pizza_size.pk, not None)

    def test_is_created_duplicate_pizza_and_name_case(self):
        """
        Pizza size with duplicate pizza and name is not created
        """
        pizza_size = PizzaSize(
            name="Normal",
            diameter = 30,
            pizza = self.pizza,
            price = Decimal(7))
        pizza_size.full_clean()
        pizza_size.save()
        pizza_size = PizzaSize(
            name="Normal",
            diameter = 31, #Slightly different price to differentiate
            pizza = self.pizza,
            price = Decimal(8)) #Slightly different price to differentiate
        with self.assertRaises(ValidationError):
            #full_clean called to check validations (MinValueValidator, MaxValueValidator)
            #   Called explicitly to not cause issues in forms
            #Another solution: use a ModelForm
            pizza_size.full_clean() 
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError

    def test_is_created_with_different_names_case(self):
        """
        Pizza size with same pizza but different names is created
        """
        pizza_size = PizzaSize(
            name="Normal",
            diameter = 30,
            pizza = self.pizza,
            price = Decimal(7))
        pizza_size.full_clean()
        pizza_size.save()
        pizza_size = PizzaSize(
            name="More Normal",
            diameter = 30,
            pizza = self.pizza,
            price = Decimal(7))
        pizza_size.full_clean()
        pizza_size.save()
        self.assertTrue(pizza_size.pk, not None)

    def test_is_created_with_same_name_different_pizza_case(self):
        """
        Pizza size with same name but different pizza is created
        """
        pizza_size = PizzaSize(
            name="Normal",
            diameter = 30,
            pizza = self.pizza,
            price = Decimal(7))
        pizza_size.full_clean()
        pizza_size.save()

        topping = Topping(name="Mozzarella")
        topping.save()
        pizza = Pizza(name="Mozzarella Pizza")
        pizza.save()
        pizza.toppings.add(topping)

        pizza_size = PizzaSize(
            name="Normal",
            diameter = 30,
            pizza = pizza,
            price = Decimal(7))
        pizza_size.full_clean()
        pizza_size.save()
        self.assertTrue(pizza_size.pk, not None)

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
            pizza_size.full_clean() 
            pizza_size.save()
            if pizza_size.pk is None:
                raise ValidationError

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