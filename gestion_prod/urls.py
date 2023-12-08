from django.urls import path

from gestion_prod import views
app_name='gestion_prod'

urlpatterns=[
    path('',views.list_prod, name='list_prod'),    
    path('<slug:product>/',views.product_detail,name='product_detail'),
    path('<str:slug>/add_to_cart',views.add_to_cart,name='add_to_cart'),
]