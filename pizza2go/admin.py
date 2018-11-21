from django.contrib import admin

from .models import Pizza, Topping, PizzaSize, PizzaPrice

class ToppingInline(admin.TabularInline):
    model = Topping
    extra = 2

class PizzaSizeInline(admin.TabularInline):
    model = PizzaSize
    extra = 2

class PizzaPriceInline(admin.TabularInline):
    model = PizzaPrice
    extra = 2

class PizzaInline(admin.TabularInline):
    model = Pizza
    extra = 2

class PizzaAdmin(admin.ModelAdmin):
    inlines = [PizzaSizeInline]
    
# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(PizzaSize)
admin.site.register(PizzaPrice)
admin.site.register(Topping)