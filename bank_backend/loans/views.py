from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Loan
from .forms import LoanForm

class LoanListView(LoginRequiredMixin, ListView):
    model = Loan
    template_name = 'loans/loan_list.html'
    context_object_name = 'loans'

    def get_queryset(self):
        return Loan.objects.filter(customer__user=self.request.user)  # Filtra los préstamos del usuario autenticado

class LoanDetailView(LoginRequiredMixin, DetailView):
    model = Loan
    template_name = 'loans/loan_detail.html'
    context_object_name = 'loan'

@login_required
def create_loan(request):
    customer = request.user.customer  # Asocia el préstamo al cliente autenticado
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.customer = customer
            loan.save()
            return redirect('loan_list')
    else:
        form = LoanForm()
    return render(request, 'loans/loan_form.html', {'form': form})

@login_required
def delete_loan(request, pk):
    loan = get_object_or_404(Loan, pk=pk, customer__user=request.user)
    loan.delete()
    return redirect('loan_list')