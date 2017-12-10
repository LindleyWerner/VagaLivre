from django import forms
from .models import *

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput, label="Nome", max_length=50, min_length="3")
    cpf = forms.CharField(widget=forms.TextInput, label="CPF (Somente numeros)", max_length='11', min_length="11")
    email = forms.CharField(widget=forms.EmailInput, label="Email", max_length=50, min_length="6")
    conta = forms.CharField(widget=forms.TextInput, label="Conta", max_length=20, min_length=8)
    data = forms.CharField(widget=forms.TextInput, label="Data de validade", min_length=5)
    codigo = forms.IntegerField(widget=forms.TextInput, label="Codigo de seguranca", min_value=100)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Senha", max_length=20, min_length="8")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmacao da senha", max_length=20, min_length="8")

    class Meta:
        model = User
        fields = ['username', 'cpf', 'email', 'conta', 'data', 'codigo', 'password1', 'password2']
