from rest_framework.serializers import ModelSerializer
from .models import Budget


class BudgetSerializer(ModelSerializer):
    class Meta:
        model = Budget
        fields = ('__all__')
