from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CashInAcctM, CashOutAcctM, WhatWeOwnAcctM, DebtsAcctM, NetworthAcctM, StatementLinesDetails, StatementLinesHeader

INPUT_CLASSES = 'rounded-xl border form-control'

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
        fields = ('Status', 'Type', 'AccountNumber', 'Description', 'Statement', 'Section',)
        widgets = {
            'Status': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Type': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'AccountNumber': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Statement': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Section': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'RollupType': forms.TextInput(attrs={
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

# NEW FROM HERE 
        
from .models import StatementLinesHeader, StatementLinesDetails

INPUT_CLASSES = 'rounded-xl border form-control'

class StatementLinesHeaderForm(forms.ModelForm):
    class Meta:
        model = StatementLinesHeader
        fields = ('LHName', 'LHDescription',)
        widgets = {
            'LHName': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'LHDescription': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class StatementLinesDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        StatementLinesHeaderF = kwargs.pop('StatementLinesHeader', None)  # Get the passed list_header and remove from kwargs
        super(StatementLinesDetailForm, self).__init__(*args, **kwargs)
        if StatementLinesHeaderF:
            self.fields['StatementLinesHeaderFK'].initial = StatementLinesHeaderF

            self.fields['StatementLinesDetailFK'].queryset = StatementLinesDetails.objects.filter(StatementLinesHeaderFK=list_header)

    class Meta:
        model = StatementLinesDetails
        fields = ('ListHeaderFK', 'ListDetailFK', 'SLNumber', 'SLName')
        widgets = {
            'ListHeaderFK': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'ListDetailFK': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'LHNumber': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'LHName': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
    ListHeaderFK = forms.ModelChoiceField(queryset=StatementLinesHeader.objects.all(), widget=forms.Select(attrs={'class': INPUT_CLASSES}))
    ListDetailFK = forms.ModelChoiceField(queryset=StatementLinesDetails.objects.all(), widget=forms.Select(attrs={'class': INPUT_CLASSES}), required=False)

class StatementLinesHeaderSelectForm(forms.ModelForm):
    class Meta:
        model = StatementLinesHeader
        fields = ['LHName']

    LHName = forms.ModelChoiceField(queryset=StatementLinesHeader.objects.all(), widget=forms.Select(attrs={'class': INPUT_CLASSES}))
