from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

 



# class Order
# DateField
# OrderID


# class OrderItem(models.Model)
#     user
#     OrderID = 
#     product = models.ForeignKey(Product)
#     quantiy = models.IntegerField()
# user order productid quantity
# 1     1       2         2
# 1  3   1
# 1  4   1
