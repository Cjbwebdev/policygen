"""
Custom user model + profile
"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Extended user with subscription status"""
    is_pro = models.BooleanField(default=False)
    stripe_customer_id = models.CharField(max_length=100, blank=True)
    documents_generated = models.IntegerField(default=0)

    class Meta:
        db_table = 'app_user'

    def __str__(self):
        return self.email or self.username
