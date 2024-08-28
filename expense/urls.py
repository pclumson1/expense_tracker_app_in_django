from django.urls import path
from django.urls import reverse
from .views import *


urlpatterns = [

    path('', expense_list, name='expense_list'),

    path("<uuid:pk>/", expense_detail, name="expense_detail"),

    path("statistic/", expense_statistic, name="expense_statistic"),


]
