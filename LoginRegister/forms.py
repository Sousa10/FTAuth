from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from .models import SponRates


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

class SponRatesForm(forms.ModelForm):  
    class Meta:
        model = SponRates
        fields = ('Sequence', 'Geography', 'Population', 'FTUserCount', 'Spots1_6Rate', 'Spot7Rate')
        widgets = {
            'Sequence': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Geography': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Population': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'FTUserCount': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Spots1_6Rate': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Spot7Rate': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }

# 
#   KMS Start Day Picker
# 
class DateInput(forms.DateInput):
    input_type = 'date'

class UploadExcelForm(forms.Form):
    excel_file = forms.FileField()

class TemplateActionForm(forms.Form):
    ACTION_CHOICES = [
        ('', 'Choose an action...'),
        ('download', 'Download Template'),
        ('upload', 'Upload Template'),
    ]

    action = forms.ChoiceField(choices=ACTION_CHOICES, required=True)
    excel_file = forms.FileField(required=False)