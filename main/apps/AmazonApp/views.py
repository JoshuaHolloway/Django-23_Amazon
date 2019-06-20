from django.shortcuts import render, HttpResponse
from .models import Product

def index(request):

  # TODO: Remove this initialization of the database

  # TODO: Initialize database upon first use
  # Product.objects.create(item="Shirt", price=19.99)
  # Product.objects.create(item="Shoes", price=24.99)
  # Product.objects.create(item="Cup",   price=4.99)
  # Product.objects.create(item="Book",  price=49.99)



  return render(request, "AmazonApp/index.html", {'products': Product.objects.all()})
  # return HttpResponse("hello")
