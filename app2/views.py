from turtle import title
from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from app2.models import Products, Cart, User
from app2.forms import UserCreationForm, LoginForm
from django.contrib import messages
from django.http import JsonResponse
from app2.models import Orders

get = "GET"
post = 'POST'

def home(request):
    products = Products.objects.all()
    user = request.session.get('user',None)
    return render(request, 'app2/home.html', {'products':products, 'user':user})


def new_user(request):
    if request.method == get:
        form = UserCreationForm(auto_id=True)
        return render(request, 'app2/new_user.html', {'form':form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Accout Created Successfully')
            form.save()
            return redirect('login')
        else:
            return render(request, 'app2/new_user.html', {'form':form})


def login(request):
    if request.method == get:
        form = LoginForm()
        return render(request, 'app2/login.html', {'form':form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user
            return redirect('/home/')
        else:
            return render(request, 'app2/login.html',{'form':form})


def logout(request):
    if request.session['user']:
        del request.session['user']
    return redirect('/home/')


def cart(request):
    user = request.session.get('user')
    products = Cart.objects.filter(user=user)

    total_ammount = 0
    for product in products:
        total_ammount += product.quantity*product.product.price

    if total_ammount == 0:
        return render(request, 'app2/empty_cart.html')
    else:
        context = {'products':products, 'total_ammount':total_ammount}
        return render(request, 'app2/cart.html', context)


def remove_from_cart(request):
    cart_id = request.GET.get('cart_id')
    print('remove from cart')
    c = Cart.objects.get(pk=cart_id)
    c.delete()
    return redirect('/cart/')


def increase_quantity(request):
    cart_id = request.GET.get('cart_id')
    c = Cart.objects.get(pk=cart_id)
    c.quantity += 1
    price = c.product.price
    c.save()
    data = {'price':price}
    return JsonResponse(data)


def decrease_quantity(request):
    cart_id = request.GET.get('cart_id')
    c = Cart.objects.get(pk=cart_id)
    c.quantity -= 1
    price = c.product.price
    c.save()
    data = {'price':price}
    return JsonResponse(data)


def single_product(request, product):
    product = Products.objects.get(pk=product)
    user = request.session.get('user',None)
    result = Cart.objects.filter(product=product, user=user).exists()
    context = {'product':product, 'user':user, 'add_to_cart':not result}
    return render(request, 'app2/single_product.html', context)


def buy_now(request):
    product_id = request.POST.get('product_id')
    return HttpResponse()


def add_to_cart(request):
    product = request.POST.get('product')
    user = request.session.get('user')
    product = Products.objects.get(pk=product)
    user = User.objects.get(pk=user)
    Cart.objects.create(product=product, user=user)
    return redirect('/cart/')


def place_order(request):
    user = request.session.get('user')
    products = Cart.objects.filter(user=user)

    total_ammount = 0
    for product in products:
        total_ammount += product.quantity*product.product.price

    return render(request, 'app2/place_order.html', {
        'products':products,
        'total_ammount':total_ammount
        })


def pay(request):
    user = request.session.get('user')
    products = Cart.objects.filter(user=user)
    user = User.objects.get(pk=user)

    for product in products:
        Orders(user=user, product=product.product, quantity=product.quantity).save()

    return redirect('orders')


def orders(request):
    user = request.session.get('user')
    products = Orders.objects.filter(user=user)
    if len(products) == 0:
        return render(request, 'app2/no_order.html')
    else:
        return render(request, 'app2/orders.html', {'products':products})



