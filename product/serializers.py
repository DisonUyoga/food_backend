from rest_framework import serializers
from .models import Category , Product, Review, RelatedProductImage


class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model=Category
    fields=(
      "id",
      "title",
      "created_at",
      "created_by"
    )
class RelatedProductImageSerializer(serializers.ModelSerializer):
  class Meta:
    model=RelatedProductImage
    fields=(
      "id",
      "relatedProductImage"
    )
class ProductSerializer(serializers.ModelSerializer):

  category=CategorySerializer(read_only=True)

  relatedImage=serializers.SerializerMethodField(read_only=True)
  class Meta:
    model=Product
    fields=(
      "id",
      "productName",
      "category",
      "price",
      "description",
      "productImage",
      "relatedImage"

    )
  def get_relatedImage(self,obj):
    item=RelatedProductImage.objects.filter(product_id=obj.pk)
    if item is not None:
      return RelatedProductImageSerializer(item, many=True, context=self.context).data
    return None

class ReviewSerializer(serializers.ModelSerializer):
  product=ProductSerializer(read_only=True, many=True)
  class Meta:
    model=Review
    fields=(
    "id",
    "product",
    "text"
  )
