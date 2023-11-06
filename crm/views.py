from django.shortcuts import render
from .forms import OrderForm
from .models import Order


# Create your views here.
def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name = name, order_phone = phone)
        element.save()
        return render(request, './thanks.html', {'name': name, 'phone': phone})
    else:
        return render(request, './thanks.html')


