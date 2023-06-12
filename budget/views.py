from django.contrib.auth.models import User
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BudgetSerializer
from .models import Budget
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class BudgetView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data["user"] = request.user.id
        serializer = BudgetSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        # budgets = Budget.objects.filter(user=request.data.user).latest('date')
        
        try:
            ser = BudgetSerializer(instance=Budget.objects.filter(
                user_id=request.user.id).latest('date'))
            return Response(data=ser.data, status=status.HTTP_200_OK)
        except Budget.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
    # def put(self,request):
    #     budget = Budget.objects.get(id=request.data["id"])
    #     ser = BudgetSerializer(instance=budget,data=request.data,partial=True)
    #     ser.is_valid(True)
    #     ser.save()
    #     return Response(status=status.HTTP_201_CREATED)
