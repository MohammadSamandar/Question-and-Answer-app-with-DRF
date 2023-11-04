from rest_framework import serializers

class ProductSerializers(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.IntegerField()
    slug = serializers.SlugField()