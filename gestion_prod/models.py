from django.db import models
from django.urls import reverse
from django.utils import timezone
from Gestion_Produits.settings import AUTH_USER_MODEL
from accounts.models import User


# Create your models here.
class Categorie(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) :
            return self.name

class StockedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(stock__gt=0)
        
class Product(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=250)
    stock=models.IntegerField(default=0)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    description=models.TextField(default="",blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    thembnail=models.ImageField(upload_to="products_img", blank=True, null=True)
    objects=models.Manager()
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='products_user')
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='products')
    InStock=StockedManager()
    def get_absolute_url (self):
        return reverse('gestion_prod:product_detail', 
                       args=[self.slug])
    class Meta:
        ordering = ['-price']
        indexes=[models.Index(fields=['-stock'])]   
        def __str__(self) :
            return self.name

class Ordre(models.Model):
    user= models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantite= models.IntegerField(default=1)
    ordred= models.BooleanField(default=False)

    def __str__(self):
         return f"{self.product.name} ({self.quantite})"
     
class Cart(models.Model):
     user = models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
     orders = models.ManyToManyField(Ordre)
     ordered = models.BooleanField(default=False)
     ordered_date= models.DateTimeField(blank=True, null=True)
     def __str__(self):
         return self.user.username
