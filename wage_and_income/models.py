from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class WageAndIncome(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    # 0 or False means wage, 1 or True mean income
    type = models.BooleanField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
