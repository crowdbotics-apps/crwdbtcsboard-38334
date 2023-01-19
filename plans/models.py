from django.conf import settings
from django.db import models
class Plan(models.Model):
    'Generated Model'
    name = models.CharField(max_length=50,)
    description = models.TextField(null=True,blank=True,max_length=255)
    price = models.DecimalField(null=True,blank=True,max_digits=5,decimal_places=2,)
    created_at = models.DateTimeField(null=True,blank=True,auto_now_add=True,)
    updated_at = models.DateTimeField(null=True,blank=True,auto_now_add=True,)

    def __str__(self):
        return f"{self.name} - {self.price}"