from django import forms
from django.contrib.auth.models import User
from .models import *

class quartoForms(forms.ModelForm):
    class Meta:
        model = quarto
        fields = ['num_Quarto','qtd_Hospedes','tipo','valor','descricao', 'img']

class AtendenteForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()  
        }

class HospedeForms(forms.ModelForm):
    class Meta:
        model = hospede
        fields = ['nome', 'cpf', 'data_inicio', 'data_final']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_final': forms.DateInput(attrs={'type': 'date'}),
        }
