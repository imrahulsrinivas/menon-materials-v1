from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import UnreadablePostError, Http404, HttpResponse
from .models import *
from core.models import Customer

@login_required
def index(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    total_orders_delivered = orders.filter(status="Delivered").count()
    totaL_orders_pending = orders.filter(status="Pending").count()
    context = {
        'customers':customers,
        'orders':orders,
        'total_orders_delivered':total_orders_delivered,
        'total_orders_pending':totaL_orders_pending,
        'total_orders':total_orders,
    }
    return render(request, 'marketing/index.html', context)
    
@login_required
def product(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'marketing/product.html', context)


    