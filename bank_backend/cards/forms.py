from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['card_number', 'card_type', 'expiration_date', 'cvv']
        widgets = {
            'card_number': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 16}),
            'card_type': forms.TextInput(attrs={'class': 'form-control'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cvv': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 3}),
        }