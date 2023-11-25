
from django.db import models
from django.conf import settings

User=settings.AUTH_USER_MODEL

class Category(models.Model):
  created_by=models.ForeignKey(User, default=1, on_delete=models.CASCADE)
  title=models.CharField(max_length=255)
  created_at=models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural="Categories"

  def __str__(self):
    return self.title



class Product(models.Model):
  category=models.ForeignKey(Category, on_delete=models.CASCADE)
  productName=models.CharField(max_length=255)
  price=models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
  description=models.TextField()
  productImage=models.ImageField(upload_to="media/")
  

  def __str__(self):
    return self.productName

class RelatedProductImage(models.Model):
  product=models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='related_image', blank=True, null=True)
  relatedProductImage=models.ImageField(upload_to="media")
  
class Review(models.Model):
  product=models.ForeignKey(Product, on_delete=models.CASCADE)
  name=models.CharField(max_length=255)
  text=models.TextField()

  def __str__(self):
    return self.text


