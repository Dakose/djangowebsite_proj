from django.shortcuts import render
from .forms import OrderForm
from .models import Order
from testimonials.models import TestimonialsSlider

def first_page(request):
    testimonials = TestimonialsSlider.objects.all()
    form = OrderForm()
    dict_obj = {
        'testimonials': testimonials,
        'form': form,
        }
    return render(request, './home.html', dict_obj)

# Create your views here.
def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        element = Order(order_name = name, order_email = email, order_phone = phone)
        element.save()
        return render(request, './thanks.html', {'name': name, 'email': email, 'phone': phone})
    else:
        return render(request, './thanks.html')

