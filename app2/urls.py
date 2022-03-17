from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name="home"),
    path('new_user/', views.new_user, name="new_user"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('single_product/<int:product>', views.single_product),
    path('cart/', views.cart, name="cart"),
    path('orders/', views.orders, name="orders"),
    path('buy_now/', views.buy_now, name="buy_now"),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('increase_quantity/', views.increase_quantity, name="increase_quantity"),
    path('decrease_quantity/', views.decrease_quantity, name="decrease_quantity"),
    path('remove_from_cart/', views.remove_from_cart, name="remove_from_cart"),
    path('place_order/', views.place_order, name="place_order"),
    path('pay/' , views.pay, name="pay")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
