from rest_framework import serializers
from .models import Shop, Category, Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())
    image = serializers.SerializerMethodField()# hoặc serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'slug', 'description', 'categories']
