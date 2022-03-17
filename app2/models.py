from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)


CATEGORY = (
    ('Mobile','Mobile'),
    ('Laptop','Laptop'),
    ('Top Wears','Top Wears'),
    ('Bottom Wears','Bottom Wears')
)



class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY, max_length=100)
    image = models.ImageField(upload_to='product_images')


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


STATUS = (
    ('Packed','Packed'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, default='Pending', max_length=100)
