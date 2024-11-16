from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'customer', 'amount']

    def clean_customer(self):
        customer = self.cleaned_data.get('customer')
        return customer
