from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    ACCOUNT_TYPES = [
        ('Black', 'Black'),
        ('Gold', 'Gold'),
        ('Classic', 'Classic'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, default='Classic')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"