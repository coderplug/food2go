from django.contrib import admin

from .models import Pizza, Topping, PizzaSize, UserShoppingCart

class ToppingInline(admin.TabularInline):
    model = Topping
    extra = 2

class PizzaSizeInline(admin.TabularInline):
    model = PizzaSize
    extra = 2

class PizzaInline(admin.TabularInline):
    model = Pizza
    extra = 2

class PizzaAdmin(admin.ModelAdmin):
    inlines = [PizzaSizeInline]
    
# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(PizzaSize)
admin.site.register(Topping)
admin.site.register(UserShoppingCart)