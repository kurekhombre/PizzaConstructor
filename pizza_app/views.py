from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import OptionGroup, Option, ToppingGroup, Topping, Order, OrderOption, OrderTopping
from .forms import OrderForm


@csrf_protect
def index(request):
    if request.method == 'POST':
        order = Order()
        order.save(force_insert=True)
        for key, value in request.POST.items():
            if key == "Size" or key == "Crust":
                option = Option.objects.get(name=value)
                OrderOption.objects.create(order=order, option=option)
            if value.isdigit():
                topping = Topping.objects.get(name=key)
                amount = int(value)
                OrderTopping.objects.create(order=order, topping=topping, amount=amount)

        return redirect('order', order_id=order.pk)
    else:
        return render(request, 'pizza_app/index.html', {
            'options_groups': OptionGroup.objects.all(),
            'toppings_groups': ToppingGroup.objects.all()
        })


@csrf_protect
def order(request, order_id):
    customer_order = get_object_or_404(Order, pk=order_id)
    order_price = customer_order.price
    order_created = customer_order.created
    order_options = OrderOption.objects.filter(order=customer_order)
    order_toppings = OrderTopping.objects.filter(order=customer_order)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            customer_order = form.save()
            customer_order.save()
            customer_name = customer_order.customer_name
            customer_email = customer_order.customer_email

            subject = f"Order number {order_id}"
            message = f"Hi {customer_name}! \n"
            message += f"You have ordered a pizza at: {order_created}\n"
            message += f"You choosed: \n"
            for order_option in order_options:
                message += f" - {order_option.option.name}: {order_option.option.price}$\n"
            for order_topping in order_toppings:
                message += f" - {order_topping.topping.name}: {order_topping.topping.price}$ * {order_topping.amount} = {order_topping.price}$\n"
            message += f"Total price: {order_price}$\n"
            sender_mail = settings.DEFAULT_FROM_EMAIL
            send_mail(subject, message, sender_mail,
                      (sender_mail, customer_email), fail_silently=False)
            messages.success(request, "An email confirmation has been sent!")
        else:
            messages.error(request, "Invalid data")
        return redirect('message')

    form = OrderForm()
    return render(request, 'pizza_app/order.html', {
       'form': form,
       'order_id': order_id,
       'order_price': order_price,
       'order_created': order_created,
       'order_options': order_options,
       'order_toppings': order_toppings,
   })


def message(request):
    return render(request, 'base.html')