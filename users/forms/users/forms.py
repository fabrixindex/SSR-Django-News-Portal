from django import forms
from django.contrib.auth.forms import UserCreationForm
from ...models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#! REVISAR
#? SIMPLIFICAR

class UserForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'placeholder': 'Tell us about yourself'}))
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)  # Guarda el usuario (sin el perfil)

        # Aquí es donde asignamos los campos adicionales
        if 'bio' in self.cleaned_data:
            user.bio = self.cleaned_data['bio']  # Agregar bio al campo del usuario (esto lo tendrás que agregar en el modelo si es necesario)
        if 'birth_date' in self.cleaned_data:
            user.birth_date = self.cleaned_data['birth_date']  # Agregar birth_date al campo del usuario

        if commit:
            user.save()  # Guarda el usuario con los nuevos campos adicionales

        return user

