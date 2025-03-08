from django.db import models

# Create your models here.
from django.db import models
class Transaction(models.Model):
    date=models.DateField()
    description=models.CharField(max_length=255)
    credit=models.FloatField(default=0.0)
    debit=models.FloatField(default=0.0)
    running_balance=models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.description}-{self.running_balance}"
    