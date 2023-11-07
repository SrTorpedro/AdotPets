from django.db import models
from auth_user.models import Company

from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    desc = models.CharField(max_length=250)
    value = models.FloatField()
    fk_company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='product')
    category = models.CharField(max_length=50, null=False)
    discount = models.FloatField(null=True, blank=True)

class ProductImage(models.Model):
    fk_product = models.ForeignKey(Product, related_name='image', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='product_image')

class ShoppingCart(models.Model):
    fk_product = models.ForeignKey(Product, related_name='shoppingCartProduct', on_delete=models.CASCADE)
    fk_user = models.ForeignKey(User, related_name='shoppingCartUser', on_delete=models.CASCADE)
    ammount = models.IntegerField()

class ProductOrder(models.Model):
    fk_user = models.ForeignKey(User, related_name='productOrderClient', on_delete=models.CASCADE)
    fk_company = models.ForeignKey(User, related_name='productOrderCompany', on_delete=models.CASCADE)
    city = models.CharField(max_length=90)
    road = models.CharField(max_length=125)
    number = models.IntegerField()
    complement = models.CharField(max_length=120)
    sent = models.BooleanField(default=False)

class OrderIten(models.Model):
    fk_product = models.ForeignKey(Product, related_name='orderItemProduct', on_delete=models.CASCADE)
    fk_order = models.ForeignKey(ProductOrder, related_name='order', on_delete=models.CASCADE)
    ammount = models.IntegerField()