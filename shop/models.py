from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=500)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    discount_price = models.FloatField(validators=[MinValueValidator(0.0)])
    category = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    image = models.CharField(max_length=1000, 
    default='https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg')

class Order(models.Model):
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.name

    items = models.TextField()
    total = models.PositiveIntegerField()
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    zipcode = models.PositiveIntegerField(blank=False)
    address = models.TextField(max_length=1000, blank=False)

    
