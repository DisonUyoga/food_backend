from django.urls import path
from . import views


urlpatterns = [
    path("", views.product_view, name="product-list"),
    path("review/", views.review_view, name="review-create")
]
