from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from budget.models import Budget
from budget.serializers import BudgetSerializer
from .serializers import WageAndIncomeSerializer
from .models import WageAndIncome
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from copy import deepcopy

class WageAndIncomeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data["user"] = request.user.id
        w_i_serializer = WageAndIncomeSerializer(data=data)
        w_i_serializer.is_valid(raise_exception=True)
        w_i_serializer.save()
        budget_serializer = BudgetSerializer(
            instance=Budget.objects.filter(user_id=request.user.id).latest('date'))
        budget_amount = float(budget_serializer.data["amount"])
        w_i_amount = float(w_i_serializer.data["amount"])
        if(w_i_serializer.data["type"] == True):
            budget_amount += w_i_amount
        if(w_i_serializer.data["type"] == False):
            budget_amount -= w_i_amount
        dict=deepcopy(budget_serializer.data)
        dict.__setitem__("amount",budget_amount)
        dict.pop("date")     
        budget_serializer = BudgetSerializer(data=dict)
        if(budget_serializer.is_valid(raise_exception=True)):
            budget_serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        wi=WageAndIncome.objects.filter(user_id=request.user.id,date__year=datetime.now().year).order_by('-date')
        ser = WageAndIncomeSerializer(instance=wi, many=True)
        income_sum=wi.filter(date__month=datetime.now().month,type=True).aggregate(total_income=Sum('amount'))
        wage_sum=wi.filter(date__month=datetime.now().month,type=False).aggregate(total_wage=Sum('amount'))
        if(income_sum['total_income']==None):
            income_sum['total_income']=0
        if(wage_sum['total_wage']==None):
            wage_sum['total_wage']=0
        dict = {
            'wageNincome':ser.data,
            'totalIncome':income_sum['total_income'],
            'totalWage':wage_sum['total_wage']
        }
        return Response(data=dict, status=status.HTTP_200_OK)
    # def put(self,request):
    #     w_i = WageAndIncome.objects.get(id=request.data["id"])
    #     ser = WageAndIncomeSerializer(instance=w_i,data=request.data,partial=True)
    #     ser.is_valid(True)
    #     ser.save()
    #     return Response(status=status.HTTP_201_CREATED)
