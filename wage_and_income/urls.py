from django.urls import path
from .views import WageAndIncomeView


urlpatterns = [
    path("", WageAndIncomeView.as_view(), name="signup"),

]
