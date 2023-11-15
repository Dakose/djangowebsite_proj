from django.shortcuts import render
from .forms import OrderForm
from .models import Order

def first_page(request):
    form = OrderForm()
    dict_obj = {
        'form': form,
    }
    return render(request, './home.html', dict_obj)

# Create your views here.
def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        element = Order(order_name = email, order_phone = phone)
        element.save()
        return render(request, './thanks.html', {'name': name, 'email': email, 'phone': phone})
    else:
        return render(request, './thanks.html')

