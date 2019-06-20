from django.db import models

# Create your models here.
class Product(models.Model):
  #id
  item = models.CharField(max_length=128)
  price = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"Users: ({self.item}, {self.price})"