from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'customer', 'amount', 'description']
        widgets = {
            'transaction_type': forms.Select(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        error_messages = {
            'transaction_type': {
                'required': "Por favor, selecciona un tipo de transacción.",
            },
            'customer': {
                'required': "Por favor, selecciona un cliente.",
            },
            'amount': {
                'required': "El monto es obligatorio.",
                'invalid': "Por favor, ingresa un monto válido.",
            },
            'description': {
                'required': "Por favor, ingresa una descripción.",
            },
        }

    def clean_customer(self):
        customer = self.cleaned_data.get('customer')
        return customer
