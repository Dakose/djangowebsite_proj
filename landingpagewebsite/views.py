from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from crm.models import Order
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import UserSerializer, GroupSerializer, OrderSerializer


def first_page(request):
    return render(request, './home.html')

def thanks_page(request):
    return render(request, './thanks.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]