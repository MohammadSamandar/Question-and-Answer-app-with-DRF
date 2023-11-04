from django.shortcuts import render, get_object_or_404
from .models import Product
from rest_framework.views import APIView
from .Serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import Http404
# Create your views here.


class ProductList(APIView):
    # permission_classes = [IsAdminUser]

    def get(self, requset):
        products = Product.objects.all()
        ser_data = ProductSerializers(instance=products, many=True)
        return Response(data=ser_data.data)
    # return render(request, 'product_module/product_list.html', {'products': products})


def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)

    return render(request, 'product_module/product_detail.html', {'product' : product})
