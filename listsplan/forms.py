from django import forms

from .models import ListHeaderT, ListDetailsT

INPUT_CLASSES = 'rounded-xl border form-control'

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

class ListDetailsTForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        list_header = kwargs.pop('list_header', None)  # Get the passed list_header and remove from kwargs
        super(ListDetailsTForm, self).__init__(*args, **kwargs)
        if list_header:
            self.fields['ListHeaderFK'].initial = list_header

            self.fields['ListDetailFK'].queryset = ListDetailsT.objects.filter(ListHeaderFK=list_header)

    class Meta:
        model = ListDetailsT
        fields = ('ListHeaderFK', 'ListDetailFK', 'LNNumber', 'LHName')
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
        }
    ListHeaderFK = forms.ModelChoiceField(queryset=ListHeaderT.objects.all(), widget=forms.Select(attrs={'class': INPUT_CLASSES}))
    ListDetailFK = forms.ModelChoiceField(queryset=ListDetailsT.objects.all(), widget=forms.Select(attrs={'class': INPUT_CLASSES}), required=False)

class ListHeaderSelectForm(forms.ModelForm):
    class Meta:
        model = ListHeaderT
        fields = ['LHName']

    LHName = forms.ModelChoiceField(queryset=ListHeaderT.objects.all(), widget=forms.Select(attrs={'class': INPUT_CLASSES}))
