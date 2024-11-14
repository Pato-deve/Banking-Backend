from django import forms
from django.contrib.auth.models import User

from .models import Customer

class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)  # Campo adicional para el perfil de Customer

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Asegúrate de guardar la contraseña de forma segura

        if commit:
            user.save()
            # Crear el perfil Customer al guardar el usuario
            Customer.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                phone=self.cleaned_data['phone']
            )
        return user