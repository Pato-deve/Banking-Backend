from django.db import models
from customers.models import Customer

class Card(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, unique=True)
    card_type = models.CharField(max_length=50)
    expiration_month = models.PositiveSmallIntegerField()
    expiration_year = models.PositiveSmallIntegerField()
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.card_type} - {self.card_number[-4:]}"