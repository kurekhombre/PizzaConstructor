from django.contrib import admin
from .models import OptionGroup, Option, ToppingGroup, Topping, Order, OrderOption, OrderTopping

admin.site.register([OptionGroup, Option, ToppingGroup, Topping, Order, OrderOption, OrderTopping])
