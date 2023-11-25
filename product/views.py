from rest_framework import generics
from .serializers import ProductSerializer, ReviewSerializer
from .models import Product, Review


class ProductListAPIView(generics.ListAPIView):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer

product_view=ProductListAPIView.as_view()


class ReviewCreateAPIView(generics.CreateAPIView):
  queryset=Review.objects.all()
  serializer_class=ReviewSerializer

review_view=ReviewCreateAPIView.as_view()

