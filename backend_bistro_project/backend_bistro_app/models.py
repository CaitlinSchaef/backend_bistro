from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'Customer Name: {self.name}, Customer ID: {self.id}'
    
class EmployeeDriver(models.Model):
    name = models.CharField(max_length=50, null=True)
    

class CustomerReview(models.Model):
    number_of_stars = (
                        ('1', '1'),
                        ('2', '2'),
                        ('3', '3'),
                        ('4', '4'),
                        ('5', '5')
                        )
    customer_name = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    stars = models.CharField(choices=number_of_stars, null=True, max_length=5)
    review_body = models.CharField(max_length=1500, null=True)

    def __str__(self):
        return f'Name: {self.customer_name}, Rating: {self.stars} Stars, Review: {self.review_body}'

class MenuCategory(models.Model):
    category = models.CharField(max_length=60, null=True)

class MenuItem(models.Model):
    name = models.CharField(max_length=40, null=True)
    price = models.PositiveIntegerField(default=12, null=True)
    description = models.CharField(max_length=150, null=True)
    category = models.ManyToManyField(MenuCategory)

    def __str__(self):
        return f'Item Name: {self.name}, Category: {self.category}, Description: {self.description}, Price: {self.price}'
    

class OrderStatus(models.Model):
    status = models.CharField(max_length=60, null=True)
    paid = models.BooleanField(default=False)
    location = models.CharField(max_length=50, null=True)
    
    #not only status of order being prepared, but also paid
    def __str__(self):
        return f'Order is {self.status} and is {self.paid}'
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
    delivery_driver = models.ForeignKey(EmployeeDriver, null=True, on_delete=models.SET_NULL)
    delivery_tip = models.PositiveIntegerField(default=5, null=True)
    # your view set can return things that aren't on there! So we will do total price then and tip.


# Okay, so they will have to make their order first, and then basically fill the order with menu items which is annoying but whatever 

class OrderItem(models.Model):
    customer_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item_on_order = models.ForeignKey(MenuItem, null=True, on_delete=models.SET_NULL, related_name='food_item_on_order')
    food_selection_quantity = models.PositiveIntegerField(default=1)
    order_modifications = models.CharField(max_length=400, null=True)


    # order_status_options = (
    #                         ('Awaiting Confirmation', 'Awaiting Confirmation'),
    #                         ('Preparing Order', 'Preparing Order'),
    #                         ('Ready For Pickup', 'Ready for Pickup'),
    #                         ('Order Complete', 'Order Complete')
    #                         )