
from django.db.models import Sum, Max, Min, Avg
from django.shortcuts import render, get_object_or_404
from expense.models import Expense


# Create your views here.
def expense_statistic(request):
    data = Expense.objects.aggregate(sum=Sum('price'), max=Max('price'), min=Min('price'), avg=Avg('price'))
    return render(request, 'e_statistic.html', {"data":data})


def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    return render(request, "post_detail.html", {"expense": expense})

def expense_list(request):
    expenses = Expense.objects.all()
    data = Expense.objects.aggregate(sum=Sum('price'), max=Max('price'), min=Min('price'), avg=Avg('price'))
    return render(request, "index.html", {'expenses': expenses})
