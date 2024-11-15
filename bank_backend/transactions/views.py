from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction, TransactionType
from .forms import TransactionForm
from customers.models import Customer

@login_required
def transaction_list(request):
    transactions = Transaction.objects.all()  # Obtener todas las transacciones
    return render(request, 'transactions/transactions_list.html', {'transactions': transactions})

@login_required
def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)  # Obtener la transacción por su ID
    return render(request, 'transactions/transactions_detail.html', {'transaction': transaction})



@login_required
def transaction_create(request):
    customers = Customer.objects.all()  # Obtener todos los clientes
    transaction_types = TransactionType.objects.all()  # Obtener todos los tipos de transacción

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()  # Guardar la transacción en la base de datos
            # Redirigir a la página de detalles de la transacción
            return redirect('transaction_detail', pk=transaction.pk)
    else:
        form = TransactionForm()

    return render(request, 'transactions/transactions_form.html', {
        'form': form,
        'customers': customers,  # Pasar los clientes al template
        'transaction_types': transaction_types  # Pasar los tipos de transacciones al template
    })

@login_required
def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_detail', pk=transaction.pk)
    else:
        form = TransactionForm(instance=transaction)
    
    return render(request, 'transactions/transactions_form.html', {'form': form})
