from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Budget(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return str(self.amount)
