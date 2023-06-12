from rest_framework.serializers import ModelSerializer
from .models import WageAndIncome


class WageAndIncomeSerializer(ModelSerializer):
    class Meta:
        model = WageAndIncome
        fields = ('__all__')
