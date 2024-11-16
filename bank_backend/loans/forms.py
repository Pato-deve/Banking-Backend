from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['loan_type', 'amount', 'interest_rate', 'start_date', 'end_date']
        widgets = {
            'loan_type': forms.Select(choices=Loan.LOAN_TYPE_CHOICES, attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'interest_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        self.customer = kwargs.pop('customer', None)
        super().__init__(*args, **kwargs)

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        loan_limits = {
            'Black': 500000,
            'Gold': 300000,
            'Classic': 100000,
        }

        customer = self.customer
        if customer:
            loan_type = customer.account_type
            max_loan_amount = loan_limits.get(loan_type, 0)

            if amount > max_loan_amount:
                raise forms.ValidationError(
                    f"El monto solicitado excede el límite para su tipo de cliente ({loan_type}). "
                    f"El límite es ${max_loan_amount}."
                )

        return amount