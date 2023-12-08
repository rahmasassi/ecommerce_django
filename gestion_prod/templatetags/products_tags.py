from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
from gestion_prod.models import Product


register = template.Library()

@register.simple_tag
def total_products():
    return Product.objects.count()

@register.inclusion_tag('gestion_prod/product/latest_posts.html')
def show_latest_products (count=5):
    latest_products = Product.objects.order_by('-stock')[:count]
    return {'latest_products': latest_products}



