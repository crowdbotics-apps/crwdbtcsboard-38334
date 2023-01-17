from django.conf import settings
from django.db import models
class Subscription(models.Model):
    'Generated Model'
    user = models.IntegerField(blank=True,)
    app = models.BigIntegerField(null=True,blank=True,)
    active = models.BooleanField(null=True,blank=True,)
    created_at = models.DateTimeField(null=True,blank=True,auto_now_add=True,)
    updated_at = models.DateTimeField(null=True,blank=True,auto_now_add=True,)
    plan = models.ForeignKey("plans.Plan",on_delete=models.PROTECT,null=True,blank=True,related_name="subscription_plan",)

# Create your models here.
