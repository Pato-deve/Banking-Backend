from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
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

    # Establecer los límites de preaprobación según el tipo de cliente
    loan_limits = {
        'BLACK': 500000,
        'GOLD': 300000,
        'CLASSIC': 100000,
    }

    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.customer = customer

            # Validar si el monto solicitado está dentro del límite permitido
            loan_type = customer.user.profile.type  # Suponiendo que el tipo de cliente está en el perfil del usuario
            max_loan_amount = loan_limits.get(loan_type, 0)

            if loan.amount > max_loan_amount:
                # Si el monto solicitado excede el límite, mostrar un mensaje de error
                form.add_error('amount', f"El monto solicitado excede el límite para su tipo de cliente ({loan_type}). El límite es ${max_loan_amount}.")
                return render(request, 'loans/loan_form.html', {'form': form})

            loan.save()

            # Si la solicitud es aprobada, actualizar el saldo de la cuenta del cliente
            # Aquí deberías tener lógica para actualizar el saldo del cliente (si es necesario)
            # customer.account_balance -= loan.amount
            # customer.save()

            # Redirigir a la lista de préstamos con el mensaje de éxito
            return redirect('loan_list')
    else:
        form = LoanForm()

    return render(request, 'loans/loan_form.html', {'form': form})

@login_required
def delete_loan(request, pk):
    loan = get_object_or_404(Loan, pk=pk, customer__user=request.user)
    loan.delete()
    return redirect('loan_list')