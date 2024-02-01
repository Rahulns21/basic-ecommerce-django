from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

def index(request):
    product_objects = Product.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
    
    #pagination
    paginator = Paginator(product_objects, 8)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    context = {
        'product_objects': product_objects
    }
    return render(request, 'shop/index.html', context)

def detail(request, pk):
    product_object = Product.objects.get(pk=pk)
    context = {
        'product_object': product_object
    }
    return render(request, 'shop/detail.html', context)

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zipcode = request.POST.get('zipcode', '')
        total = request.POST.get('total', '')
        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, total=total)
        order.save()

    return render(request, 'shop/checkout.html')