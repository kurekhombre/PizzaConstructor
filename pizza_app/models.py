from django.db import models
from typing import List
from django.utils import timezone


class OptionGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Option(models.Model):
    option_group = models.ForeignKey(OptionGroup, related_name='options', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}$"


class ToppingGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topping(models.Model):
    topping_group = models.ForeignKey(ToppingGroup, related_name='toppings', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}$"


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        total_price = 0

        order_options: List[OrderOption] = self.__getattribute__("order_option_customer").all()
        for order_option in order_options:
            total_price += order_option.price

        order_toppings: List[OrderTopping] = self.__getattribute__("order_topping_customer").all()
        for order_topping in order_toppings:
            total_price += order_topping.price

        return total_price

    def __str__(self):
        return f"{self.customer_name} should pay {self.price}"


class OrderOption(models.Model):
    order = models.ForeignKey(Order, related_name='order_option_customer', on_delete=models.CASCADE)
    option = models.ForeignKey(Option, related_name='option_customer', on_delete=models.CASCADE)

    @property
    def price(self):
        return self.option.price

    def __str__(self):
        return f"{self.option.name} - {self.price}$"


class OrderTopping(models.Model):
    order = models.ForeignKey(Order, related_name='order_topping_customer', on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, related_name='topping_customer', on_delete=models.CASCADE)
    amount = models.IntegerField()

    @property
    def price(self):
        return self.topping.price * self.amount

    def __str__(self):
        return f"{self.topping.name}, amount: {self.amount} - {self.price}$"
