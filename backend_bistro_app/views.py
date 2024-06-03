from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
#can do .models as opposed to a more explicit path because we're in same folder


from .serializers import *
# we are going to use the serialized data here so we need it all

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class EmployeeDriverViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDriver.objects.all()
    serializer_class = EmployeeDriverSerializer


class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all()
    serializer_class = CustomerReviewSerializer


class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


