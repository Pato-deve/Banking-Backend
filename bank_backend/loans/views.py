from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from customers.models import Customer
from .models import Loan
from .forms import LoanForm

@login_required
def loan_list(request):
    customer = request.user.customer
    loans = Loan.objects.filter(customer=customer)

    return render(request, 'loans/loan_list.html', {'loans': loans})

class LoanDetailView(LoginRequiredMixin, DetailView):
    model = Loan
    template_name = 'loans/loan_detail.html'
    context_object_name = 'loan'

@login_required
def create_loan(request):
    customer = request.user.customer

    if request.method == 'POST':
        form = LoanForm(request.POST, customer=customer)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.customer = customer
            loan.save()
            return redirect('loan_list')
        else:
            print(form.errors)
    else:
        form = LoanForm(customer=customer)

    return render(request, 'loans/loan_form.html', {'form': form})

@login_required
def delete_loan(request, pk):
    loan = get_object_or_404(Loan, pk=pk, customer__user=request.user)
    loan.delete()
    return redirect('loan_list')