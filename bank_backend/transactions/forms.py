from django import forms
from .models import Transaction, TransactionType, Customer

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'customer', 'amount']

    def clean_customer(self):
        customer = self.cleaned_data.get('customer')
        # Add custom validation logic for customer if necessary
        return customer