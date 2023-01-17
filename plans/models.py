from django.conf import settings
from django.db import models
class Plan(models.Model):
    'Generated Model'
    name = models.CharField(max_length=20,)
    description = models.TextField(max_length=256,)
    price = models.DecimalField(max_digits=4,decimal_places=2,)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now_add=True,)

# Create your models here.
