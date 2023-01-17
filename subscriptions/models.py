from django.conf import settings
from django.db import models
class Subscription(models.Model):
    'Generated Model'
    user = models.IntegerField(blank=True,)
    plan = models.IntegerField(null=True,blank=True,)
    app = models.BigIntegerField(null=True,blank=True,)
    active = models.BooleanField(null=True,blank=True,)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True,)
    updated_at = models.DateTimeField(auto_now_add=True,null=True,blank=True,)

# Create your models here.
