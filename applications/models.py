from django.conf import settings
from django.db import models
class Application(models.Model):
    'Generated Model'
    name = models.CharField(blank=True,max_length=256,)
    description = models.TextField(null=True,blank=True,)
    type = models.CharField(null=True,blank=True,max_length=256,)
    framework = models.CharField(null=True,blank=True,max_length=256,)
    domain_name = models.CharField(null=True,blank=True,max_length=256,)
    screenshot = models.URLField(null=True,blank=True,)
    subscription = models.IntegerField(null=True,blank=True,)
    created_at = models.DateTimeField(null=True,blank=True,auto_now_add=True,)
    updated_at = models.DateTimeField(null=True,blank=True,auto_now_add=True,)
    user = models.ForeignKey("users.User",null=True,blank=True,on_delete=models.PROTECT,related_name="application_user",)

# Create your models here.
