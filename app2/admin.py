from django.contrib import admin
from app2.models import Products, Cart, Orders

@admin.register(Products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'discount', 'description', 'brand', 'category', 'image')

@admin.register(Cart)
class CratAdminModel(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')

@admin.register(Orders)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'date', 'status')
