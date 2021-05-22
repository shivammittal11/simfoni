from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    supplier_business_name = models.CharField(max_length=250, blank=True)
    supplier_address = models.TextField(default='', blank=True)
    primary_phone = models.CharField(max_length=250, blank=True)
    secondary_representative_name = models.CharField(max_length=250, blank=True)
    secondary_email = models.EmailField(max_length=250, blank=True)
    secondary_phone = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "%s" % (str(self.username))


class ProductData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "%s" % (str(self.name))
