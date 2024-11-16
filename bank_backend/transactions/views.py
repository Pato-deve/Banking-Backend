from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction
from .forms import TransactionForm
from customers.models import Customer

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(customer__user=request.user)
    return render(request, 'transactions/transactions_list.html', {'transactions': transactions})

@login_required
def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, customer__user=request.user)
    return render(request, 'transactions/transactions_detail.html', {'transaction': transaction})

@login_required
def transaction_create(request):
    customers = Customer.objects.filter(user=request.user)

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            if transaction.customer.user != request.user:
                return redirect('transaction_list')
            transaction.save()
            return redirect('transaction_detail', pk=transaction.pk)
    else:
        form = TransactionForm()

    return render(request, 'transactions/transactions_form.html', {
        'form': form,
        'customers': customers
    })

@login_required
def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, customer__user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_detail', pk=transaction.pk)
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'transactions/transactions_form.html', {'form': form})
