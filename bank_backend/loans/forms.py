from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['loan_type', 'amount', 'interest_rate', 'start_date', 'end_date']
        widgets = {
            'loan_type': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'interest_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_amount(self):
        # Obtener el monto solicitado
        amount = self.cleaned_data.get('amount')
        customer = self.instance.customer

        # Establecer los límites de preaprobación según el tipo de cliente
        loan_limits = {
            'BLACK': 500000,
            'GOLD': 300000,
            'CLASSIC': 100000,
        }

        loan_type = customer.user.profile.type  # Suponiendo que el tipo de cliente está en el perfil del usuario
        max_loan_amount = loan_limits.get(loan_type, 0)

        # Validar si el monto solicitado está dentro del límite permitido
        if amount > max_loan_amount:
            raise forms.ValidationError(f"El monto solicitado excede el límite para su tipo de cliente ({loan_type}). El límite es ${max_loan_amount}.")

        return amount