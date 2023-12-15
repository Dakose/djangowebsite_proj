from django.shortcuts import render
from .forms import OrderForm
from .models import Order
from testimonials.models import TestimonialsSlider
from latestnews.models import NewsSlider
from ourservice.models import ServiceSlider
from aboutus.models import AboutUs

def first_page(request):
    ourservice = ServiceSlider.objects.all()
    aboutus = AboutUs.objects.all()
    testimonials = TestimonialsSlider.objects.all()
    latestnews = NewsSlider.objects.all()
    form = OrderForm()
    dict_obj = {
        'ourservice': ourservice,
        'aboutus': aboutus,
        'testimonials': testimonials,
        'latestnews': latestnews,
        'form': form,
        }
    return render(request, './index.html', dict_obj)

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

