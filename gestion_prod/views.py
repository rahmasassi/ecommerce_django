from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gestion_prod.models import Product

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from gestion_prod.models import Cart, Ordre, Product

# Create your views here.
def list_prod(request):
    list_prod = Product.InStock.all()
    paginator = Paginator(list_prod, 3)
    page_number = request.GET.get('page', 1)
    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'gestion_prod/product/list.html', {'products': list_prod})

def product_detail(request, product):
    product=get_object_or_404(Product,slug=product)
    return render(request,'gestion_prod/product/detail.html',{"product":product})

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ =Cart.objects.get_or_create(user=user)
    ordre, created = Ordre.objects.get_or_create(user=user,
                                                  product=product)
    if created:
        cart.orders.add(ordre)
        cart.save()
    else:
        ordre.quantite += 1
        ordre.save()
    return redirect('gestion_prod:list_prod')

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'gestion_prod/product/cart.html', {"orders": cart.orders.all()})