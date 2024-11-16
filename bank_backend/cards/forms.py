from django import forms
from .models import Card


class CardForm(forms.ModelForm):
    CARD_TYPE_CHOICES = [
        ('Debit', 'Debit'),
        ('Credit', 'Credit'),
    ]

    MONTH_CHOICES = [(i, f"{i:02}") for i in range(1, 13)]
    YEAR_CHOICES = [(year, year) for year in range(2023, 2033)]

    card_type = forms.ChoiceField(choices=CARD_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    expiration_month = forms.ChoiceField(choices=MONTH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    expiration_year = forms.ChoiceField(choices=YEAR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Card
        fields = ['card_number', 'card_type', 'expiration_month', 'expiration_year', 'cvv']
        widgets = {
            'card_number': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 16}),
            'cvv': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 3}),
        }

    def clean_expiration_month(self):
        expiration_month = self.cleaned_data.get('expiration_month')
        expiration_month = int(expiration_month)
        if expiration_month < 1 or expiration_month > 12:
            raise forms.ValidationError("El mes de expiración debe estar entre 1 y 12.")
        return expiration_month

    def clean_expiration_year(self):
        expiration_year = self.cleaned_data.get('expiration_year')
        expiration_year = int(expiration_year)
        if expiration_year < 2023 or expiration_year > 2032:
            raise forms.ValidationError("El año de expiración debe estar dentro del rango permitido.")
        return expiration_year