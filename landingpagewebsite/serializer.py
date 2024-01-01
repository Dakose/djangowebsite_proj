from django.contrib.auth.models import User, Group
from rest_framework import serializers
from crm.models import Order

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    lookup_field = 'slug'

    class Meta:
        model = Order
        fields = ['order_dt', 'order_name', 'order_email', 'order_phone', 'order_status']

