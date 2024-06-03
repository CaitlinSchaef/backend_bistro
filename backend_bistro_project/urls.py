"""
URL configuration for backend_bistro_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework import routers
from django.urls import path, include


from backend_bistro_app.views import *
#giving it the app folder and the views from that

router = routers.DefaultRouter()

router.register(r'customer', CustomerViewSet)
router.register(r'employeeDriver', EmployeeDriverViewSet)
router.register(r'customerReview', CustomerReviewViewSet)
router.register(r'menuCategory', MenuCategoryViewSet)
router.register(r'menuItem', MenuItemViewSet)
router.register(r'orderStatus', OrderStatusViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderItem', OrderItemViewSet)

#making a path and then we're making it include all of the paths in the router
urlpatterns = [
path('', include(router.urls))  
]

