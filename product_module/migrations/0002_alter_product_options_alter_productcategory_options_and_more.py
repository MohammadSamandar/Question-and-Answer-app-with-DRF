# Generated by Django 4.2.6 on 2023-10-26 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='producttag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product_categories', to='product_module.productcategory', verbose_name='categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(db_index=True, verbose_name='main descreption'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='active / not active'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_delete',
            field=models.BooleanField(verbose_name='delete / not delete'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(db_index=True, max_length=400, null=True, verbose_name='short description'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(verbose_name='active / not active'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='is_delete',
            field=models.BooleanField(verbose_name='delete / not delete'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='title',
            field=models.CharField(db_index=True, max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='url_title',
            field=models.CharField(db_index=True, max_length=200, verbose_name='title in url'),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='caption',
            field=models.CharField(db_index=True, max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='is_delete',
            field=models.BooleanField(verbose_name='delete / not delete'),
        ),
    ]
