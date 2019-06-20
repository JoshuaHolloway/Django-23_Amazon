from django.shortcuts import render, HttpResponse
from .models import Product
# ======================================================================================================================
def get_product_info(product_id):
  return {"product": Product.objects.get(id=product_id)}
# ======================================================================================================================
def index(request):
  # TODO: Initialize database upon first use
  # Product.objects.create(item="Shirt", price=19.99)
  # Product.objects.create(item="Shoes", price=24.99)
  # Product.objects.create(item="Cup",   price=4.99)
  # Product.objects.create(item="Book",  price=49.99)

  return render(request, "AmazonApp/index.html", {'products': Product.objects.all()})
# ======================================================================================================================
def checkout(request):

  # TODO: Retrieve the proper ID
  return render(request, "AmazonApp/checkout.html", get_product_info(1))
# ======================================================================================================================

# ======================================================================================================================