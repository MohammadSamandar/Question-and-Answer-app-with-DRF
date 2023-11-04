from django.db import models
from django.utils.text import slugify
# Create your models here.



class ProductCategory(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='title')
    url_title = models.CharField(max_length=200, db_index=True, verbose_name='title in url')
    is_active = models.BooleanField(verbose_name='active / not active')
    is_delete = models.BooleanField(verbose_name='delete / not delete')



    def __str__(self):
        return f'({self.title} - {self.url_title})'

    class Meta:
        verbose_name= 'Category'
        verbose_name_plural = 'Categories'




class Product(models.Model):
    title = models.CharField(max_length=300)
    category = models.ManyToManyField(ProductCategory, related_name='product_categories',
                verbose_name='categories')
    price = models.IntegerField(verbose_name='price')
    short_description = models.CharField(max_length=400, null=True, db_index=True, verbose_name='short description')
    description = models.TextField(verbose_name='main descreption', db_index=True)
    is_active = models.BooleanField(default=False, verbose_name='active / not active')
    slug = models.SlugField(default="", null=False, blank=True, max_length=250, unique=True, db_index=True)
    is_delete = models.BooleanField(verbose_name='delete / not delete')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'




class ProductTag(models.Model):
    caption = models.CharField(max_length=200, db_index=True, verbose_name='title')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')
    is_delete = models.BooleanField(verbose_name='delete / not delete')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
