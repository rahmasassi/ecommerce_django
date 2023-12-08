from django.contrib import admin

from gestion_prod.models import Cart, Categorie, Ordre, Product

# Register your models here.
# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['name', 'slug', 'author', 'stock', 'price', 'description']
    list_filter= ['price', 'author']
    search_fields = ['name', 'price']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ['author']
    ordering = ['price', 'stock']

admin.site.register(Categorie)

admin.site.register(Ordre)
admin.site.register(Cart)