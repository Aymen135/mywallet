from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from budget.models import Budget
from wage_and_income.models import WageAndIncome
from dateutil.rrule import rrule, MONTHLY
from django.db.models import Avg, Sum
from django.db.models.functions import TruncMonth
from dateutil.relativedelta import relativedelta
from copy import deepcopy


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        dict = {}
        dict2 = {}
        # prepare dates
        start_date = datetime.strptime(request.data["start_date"], "%m/%d/%Y")
        end_date = datetime.strptime(request.data["end_date"], "%m/%d/%Y")
        last_year_start_date = start_date - relativedelta(year=1)
        last_year_end_date = end_date - relativedelta(year=1)
        # get months name from dates
        labels = [dt.strftime("%B") for dt in rrule(
            MONTHLY, dtstart=start_date, until=end_date)]
        dict.__setitem__("labels", labels)
        # budget
        # this year budget
        dict2.__setitem__("thisYear", self.prepare_budget_data(
            start_date, end_date, labels, request))
        # last year budget

        dict2.__setitem__("lastYear", self.prepare_budget_data(
            last_year_start_date, last_year_end_date, labels, request))
        dict.__setitem__("budget", deepcopy(dict2))

        # income
        dict2.clear()
        # this year
        dict2.__setitem__("thisYear", self.prepare_waginc_data(
            start_date, end_date, labels, request, True))
        # last year
        dict2.__setitem__("lastYear", self.prepare_waginc_data(
            last_year_start_date, last_year_end_date, labels, request, True))
        dict.__setitem__("income", deepcopy(dict2))
        # wage
        dict2.clear()
        # this year
        dict2.__setitem__("thisYear", self.prepare_waginc_data(
            start_date, end_date, labels, request, False))
        # last year
        dict2.__setitem__("lastYear", self.prepare_waginc_data(
            last_year_start_date, last_year_end_date, labels, request, False))
        dict.__setitem__("wage", deepcopy(dict2))
        return Response(data=dict, status=status.HTTP_200_OK)

    def prepare_budget_data(self, start_date, end_date, labels, request):
        budget = Budget.objects.filter(user_id=request.user.id, date__range=[start_date, end_date]).annotate(
            month=TruncMonth('date')).values('month').annotate(avg_amount=Avg('amount'))
        values = [0 for i in range(len(labels))]
        print(budget)
        for b in budget:
            values[labels.index(b['month'].strftime("%B"))] = b['avg_amount']
        return values

    def prepare_waginc_data(self, start_date, end_date, labels, request, type):
        w_i = WageAndIncome.objects.filter(user_id=request.user.id, date__range=[start_date, end_date], type=type).annotate(
            month=TruncMonth('date')).values('month').annotate(total_amount=Sum('amount'))
        values = [0 for i in range(len(labels))]
        print(w_i)
        for i in w_i:
            values[labels.index(i['month'].strftime("%B"))] = i['total_amount']
        return values
