from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CashInAcctM
from .models import CashOutAcctM
from .models import WhatWeOwnAcctM
from .models import DebtsAcctM

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border form-control'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class CashInAcctMForm(forms.ModelForm):
    class Meta:
        model = CashInAcctM
        fields = ('AccountNumber', 'Description',)
        widgets = {
            'AccountNumber': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class CashOutAcctMForm(forms.ModelForm):
    class Meta:
        model = CashOutAcctM
        fields = ('AccountNumber', 'Description',)
        widgets = {
            'AccountNumber': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class WhatWeOwnAcctMForm(forms.ModelForm):
    class Meta:
        model = WhatWeOwnAcctM
        fields = ('AccountNumber', 'Description',)
        widgets = {
            'AccountNumber': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class DebtsAcctMForm(forms.ModelForm):
    class Meta:
        model = DebtsAcctM
        fields = ('AccountNumber', 'Description',)
        widgets = {
            'AccountNumber': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }