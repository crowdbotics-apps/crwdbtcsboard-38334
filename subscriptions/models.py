from users.models import User
from plans.models import Plan
from apps.models import Application
from django.db import models


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="subscription_user")
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name="subscription_plan")
    app = models.ForeignKey(Application, on_delete=models.PROTECT, related_name="subscription_app")
    active = models.BooleanField("Active", default=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    update_at = models.DateTimeField("Update at", auto_now_add=True)