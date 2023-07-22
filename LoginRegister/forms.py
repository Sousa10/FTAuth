from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import CashInAcctM, CashOutAcctM, WhatWeOwnAcctM, DebtsAcctM, ListHeaderT, ListDetailsT, NetworthAcctM


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


class EquityAcctMForm(forms.ModelForm):
    class Meta:
        model = NetworthAcctM
        fields = ('AccountNumber', 'Description',)
        widgets = {
            'AccountNumber': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }
       
class ListHeaderTForm(forms.ModelForm):
    class Meta:
        model = ListHeaderT
        fields = ('LHName', 'LHDescription',)
        widgets = {
            'LHName': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'LHDescription': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class ListDetailsTFrom(forms.ModelForm):
    class Meta:
        model = ListDetailsT
        fields = ('ListHeaderFK', 'ListDetailFK', 'LNNumber', 'LHName', 'LHDescription')
        widgets = {
            'ListHeaderFK': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'ListDetailFK': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'LNNumber': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'LHName': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'LHDescription': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }