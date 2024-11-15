from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction, TransactionType
from .forms import TransactionForm
from customers.models import Customer

@login_required
def transaction_list(request):
    # Filtrar transacciones por el cliente asociado al usuario logueado
    transactions = Transaction.objects.filter(customer__user=request.user)
    return render(request, 'transactions/transactions_list.html', {'transactions': transactions})

@login_required
def transaction_detail(request, pk):
    # Asegurar que el usuario solo pueda ver sus propias transacciones
    transaction = get_object_or_404(Transaction, pk=pk, customer__user=request.user)
    return render(request, 'transactions/transactions_detail.html', {'transaction': transaction})

@login_required
def transaction_create(request):
    # Filtrar clientes relacionados con el usuario actual
    customers = Customer.objects.filter(user=request.user)
    transaction_types = TransactionType.objects.all()

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            # Verificar que la transacción pertenezca al cliente del usuario actual
            if transaction.customer.user != request.user:
                return redirect('transaction_list')
            transaction.save()
            return redirect('transaction_detail', pk=transaction.pk)
    else:
        form = TransactionForm()

    return render(request, 'transactions/transactions_form.html', {
        'form': form,
        'customers': customers,
        'transaction_types': transaction_types
    })

@login_required
def transaction_update(request, pk):
    # Asegurar que el usuario solo pueda editar sus propias transacciones
    transaction = get_object_or_404(Transaction, pk=pk, customer__user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_detail', pk=transaction.pk)
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'transactions/transactions_form.html', {'form': form})
