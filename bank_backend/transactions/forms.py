from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'customer', 'amount']

    def clean_customer(self):
        # Verificar la validez del cliente (si es necesario implementar lógica adicional)
        customer = self.cleaned_data.get('customer')
        return customer
