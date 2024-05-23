from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        #what model did we attach it to? Customer
        #what fields do we want to translate:
        fields = ['id', 'name']


class EmployeeDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDriver
        #what model did we attach it to? Employee Driver
            #what fields do we want to translate:
        fields = ['id', 'name']

class CustomerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReview
        #what model did we attach it to? CustomerReview
            #what fields do we want to translate:
        fields = ['id', 'customer_name', 'stars', 'review_body' ]
    
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        #what model did we attach it to? MenuCategory
            #what fields do we want to translate:
        fields = ['id', 'category']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        #what model did we attach it to? MenuItem
            #what fields do we want to translate:
        fields = ['id', 'name', 'price', 'description', 'category']

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        #what model did we attach it to? OrderStatus
            #what fields do we want to translate:
        fields = ['id', 'status', 'paid', 'location']
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        #what model did we attach it to? Order
            #what fields do we want to translate:
        fields = ['id', 'customer', 'date_created', 'status', 'delivery_driver', 'delivery_tip']
    
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        #what model did we attach it to? OrderItem
            #what fields do we want to translate:
        fields = ['id', 'customer_order', 'menu_item_on_order', 'food_selection_quantity', 'order_modifications']



