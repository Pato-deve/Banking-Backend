from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    # Opciones de tipo de tarjeta
    CARD_TYPE_CHOICES = [
        ('Visa', 'Visa'),
        ('MasterCard', 'MasterCard'),
        ('Amex', 'American Express'),
    ]

    card_type = forms.ChoiceField(choices=CARD_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    expiration_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )
    
    class Meta:
        model = Card
        fields = ['card_number', 'card_type', 'expiration_date', 'cvv']
        widgets = {
            'card_number': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 16}),
            'cvv': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 3}),
        }

    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number')
        if Card.objects.filter(card_number=card_number).exists():
            raise forms.ValidationError("Este número de tarjeta ya existe.")
        return card_number
