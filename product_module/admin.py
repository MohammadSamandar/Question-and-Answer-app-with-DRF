from django.contrib import admin
from .models import Product, ProductTag, ProductCategory
# Register your models here.
class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug' : ['title']
    }

    list_display = ['title', 'price', 'is_active']
    list_filter = ['price', 'is_active']
    list_editable = ['price', 'is_active']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductTag)
admin.site.register(ProductCategory)