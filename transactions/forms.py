from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CashInAcctM, FinStatements, StatementSections, SectionLines, LineAccounts

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

class FinStatementsForm(forms.ModelForm):		
    class Meta:		
        model = FinStatements		
        fields = (		
                  'FSName',
                  'FSFromDate',
                  'FSThroughDate',
                  'FSPostedDate'
                 )
        widgets = {
            'FSName': forms.TextInput(attrs={
                'class': INPUT_CLASSES
                }),
                'FSFromDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES, 'type': 'date'  
                }), 
                'FSThroughDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES, 'type': 'date'  
                }),  
                'FSPostedDate': forms.DateInput(attrs={
                'class': INPUT_CLASSES, 'type': 'date'
                })
            }
        
class StatementSectionsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        statement = kwargs.pop('statement', None)  # Get the passed section and remove from kwargs
        super(StatementSectionsForm, self).__init__(*args, **kwargs)
        if statement:
            self.fields['FinStatementsFK'].initial = statement	
    class Meta:		
        model = StatementSections		
        fields = (		
            'FinStatementsFK',
            'SSName', 	
            'SSDescription'	
        )	
        widgets = {	
            'SSName': forms.TextInput(attrs={	
            'class': INPUT_CLASSES	
            }),	
            'SSDescription': forms.TextInput(attrs={	
            'class': INPUT_CLASSES	
            })
        }
        
class SectionLinesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        section = kwargs.pop('section', None)  # Get the passed section and remove from kwargs
        super(SectionLinesForm, self).__init__(*args, **kwargs)
        if section:
            self.fields['SLStatementSectionsFK'].initial = section

    class Meta:		
        model = SectionLines		
        fields = (		
                  'SLStatementSectionsFK',
                  'SLName',		
                  'SLDescription'	
	             )	
        widgets = {	
                    'SLName': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLDescription': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    })
                } 	

class LineAccountsForm(forms.ModelForm):			
    class Meta:			
        model = LineAccounts		
        fields = (			
         'LAAccount',			
         'LAAccountType',			
         'LAADescription',			
	          )				
        widgets = {		
                    'LAAccount': forms.NumberInput(attrs={			
                    'class': INPUT_CLASSES		
                    }),		
                    'LAAccountType': forms.TextInput(attrs={			
                    'class': INPUT_CLASSES		
                    }),		
                    'LAADescription': forms.TextInput(attrs={			
                    'class': INPUT_CLASSES		
                    }),		
                    }		

class SectionSelectForm(forms.ModelForm):
    class Meta:
        model = StatementSections
        fields = ['SSName']

    SSName = forms.ModelChoiceField(queryset=StatementSections.objects.all(), widget=forms.Select(attrs={'class': INPUT_CLASSES}))

class StatementSelectForm(forms.ModelForm):
    class Meta:
        model = FinStatements
        fields = ['FSName']

    FSName = forms.ModelChoiceField(queryset=FinStatements.objects.all(), widget=forms.Select(attrs={'class': INPUT_CLASSES}))