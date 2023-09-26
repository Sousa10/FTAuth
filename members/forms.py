from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
# from .models import CashInAcctM, CashOutAcctM, WhatWeOwnAcctM, DebtsAcctM, ListHeaderT, ListDetailsT, NetworthAcctM, SponRates, TransBatch
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

INPUT_CLASSES = 'rounded-xl border form-control'


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

# KMS 9/17 Below Causes Error, temporarily commenting
    # def __init__(self, *args, **kwargs):
        # super(RegisterUserForm, self).__init__(*args, **kwargs)

        # self.fields['username'].widgets.attrs['class'] = 'INPUT_CLASSES'
        # self.fields['password1'].widgets.attrs['class'] = 'form-control'
        # self.fields['password2'].widgets.attrs['class'] = 'form-control'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

# class CashInAcctMForm(forms.ModelForm):
#     class Meta:
#         model = CashInAcctM
#         fields = ('AccountNumber', 'Description',)
#         widgets = {
#             'AccountNumber': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'Description': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             })
#         }

# class CashOutAcctMForm(forms.ModelForm):
#     class Meta:
#         model = CashOutAcctM
#         fields = ('AccountNumber', 'Description',)
#         widgets = {
#             'AccountNumber': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'Description': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             })
#         }

# class WhatWeOwnAcctMForm(forms.ModelForm):
#     class Meta:
#         model = WhatWeOwnAcctM
#         fields = ('AccountNumber', 'Description',)
#         widgets = {
#             'AccountNumber': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'Description': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             })
#         }

# class DebtsAcctMForm(forms.ModelForm):
#     class Meta:
#         model = DebtsAcctM
#         fields = ('AccountNumber', 'Description',)
#         widgets = {
#             'AccountNumber': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'Description': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             })
#         }

# class EquityAcctMForm(forms.ModelForm):
#     class Meta:
#         model = NetworthAcctM
#         fields = ('AccountNumber', 'Description',)
#         widgets = {
#             'AccountNumber': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'Description': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             })
#         }

# class SponRatesForm(forms.ModelForm):  
#     class Meta:
#         model = SponRates
#         fields = ('Sequence', 'Geography', 'Population', 'FTUserCount', 'Spots1_6Rate', 'Spot7Rate')
#         widgets = {
#             'Sequence': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'Geography': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'Population': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'FTUserCount': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'Spots1_6Rate': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'Spot7Rate': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             })
#         }

# class ListHeaderTForm(forms.ModelForm):
#     class Meta:
#         model = ListHeaderT
#         fields = ('LHName', 'LHDescription',)
#         widgets = {
#             'LHName': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'LHDescription': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             })
#         }

# class ListDetailsTForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         list_header = kwargs.pop('list_header', None)  # Get the passed list_header and remove from kwargs
#         super(ListDetailsTForm, self).__init__(*args, **kwargs)
#         if list_header:
#             self.fields['ListHeaderFK'].initial = list_header

#             self.fields['ListDetailFK'].queryset = ListDetailsT.objects.filter(ListHeaderFK=list_header)

#     class Meta:
#         model = ListDetailsT
#         fields = ('ListHeaderFK', 'ListDetailFK', 'LNNumber', 'LHName')
#         widgets = {
#             'ListHeaderFK': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'ListDetailFK': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'LNNumber': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'LHName': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#         }
#     ListHeaderFK = forms.ModelChoiceField(queryset=ListHeaderT.objects.all(), widget=forms.Select(attrs={'class': INPUT_CLASSES}))
#     ListDetailFK = forms.ModelChoiceField(queryset=ListDetailsT.objects.all(), widget=forms.Select(attrs={'class': INPUT_CLASSES}), required=False)

# class ListHeaderSelectForm(forms.ModelForm):
#     class Meta:
#         model = ListHeaderT
#         fields = ['LHName']

#     LHName = forms.ModelChoiceField(queryset=ListHeaderT.objects.all(), widget=forms.Select(attrs={'class': INPUT_CLASSES}))
# # 
# #   KMS Start Day Picker
# # 
# class DateInput(forms.DateInput):
#     input_type = 'date'

# class UploadExcelForm(forms.Form):
#     excel_file = forms.FileField()

# class TransBatchForm(forms.ModelForm):
#     TransBatchName = forms.CharField(label="Batch Name", required=True)
#     TransBatchDate = forms.CharField(label="Batch Date", required=True)

#     class Meta:
#         model = TransBatch
#         fields = ['TransBatchName', 'TransBatchDate']
#         # widgets = {
#         #     'TransBatchDate': DateInput(),
#         # }

# class TemplateActionForm(forms.Form):
#     ACTION_CHOICES = [
#         ('', 'Choose an action...'),
#         ('download', 'Download Template'),
#         ('upload', 'Upload Template'),
#     ]

#     action = forms.ChoiceField(choices=ACTION_CHOICES, required=True)
#     excel_file = forms.FileField(required=False)

# class TransBatchSelectForm(forms.ModelForm):
#     class Meta:
#         model = TransBatch
#         fields = ['BatchName']

#     BatchName = forms.ModelChoiceField(queryset=TransBatch.objects.all(), widget=forms.Select(attrs={'class': INPUT_CLASSES}))