from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CashInAcctM, StatementSections, StatementLinesLine, StatementLineAccounts
from .models import TransBatch

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

class StatementSectionsForm(forms.ModelForm):		
    class Meta:		
        model = StatementSections		
        fields = (		
	            #   'SSPersonFK', 	
                  'SSName', 	
                  'SSDescription', 	
                  'SSIncomeStatementSequence', 	
                  'SSBalanceSheetStatementSequence', 		
                  'SSCashFlowStatementSequence', 	
                  'SSExpenseStatementSequence', 		
                  'SSBudgetStatementSequence'	
                 )	
        widgets = {	
	            #   'SSPersonFK': forms.TextInput(attrs={	
                #     'class': INPUT_CLASSES	
                #   }),	
	              'SSName': forms.TextInput(attrs={	
                    'class': INPUT_CLASSES	
                  }),	
	              'SSDescription': forms.TextInput(attrs={	
                    'class': INPUT_CLASSES	
                  }),		
	              'SSIncomeStatementSequence': forms.TextInput(attrs={	
                    'class': INPUT_CLASSES	
                  }),	
	              'SSBalanceSheetStatementSequence': forms.TextInput(attrs={	
                    'class': INPUT_CLASSES	
                  }),	
	              'SSCashFlowStatementSequence': forms.TextInput(attrs={	
                    'class': INPUT_CLASSES	
                  }),		
	              'SSExpenseStatementSequence': forms.TextInput(attrs={	
                    'class': INPUT_CLASSES	
                  }),	
	              'SSBudgetStatementSequence': forms.TextInput(attrs={	
                    'class': INPUT_CLASSES	
                  }),	
                  }
        
class StatementLinesLineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        section = kwargs.pop('section', None)  # Get the passed section and remove from kwargs
        super(StatementLinesLineForm, self).__init__(*args, **kwargs)
        if section:
            self.fields['SLStatementSectionFK'].initial = section

            self.fields['SLStatementLineFK'].queryset = StatementLinesLine.objects.filter(SLStatementSectionFK=section)

    class Meta:		
        model = StatementLinesLine		
        fields = (		
                  'SLStatementSectionFK',		
                  'SLStatementLineFK',		
                  'SLName',		
                  'SLDescription',		
                  'SLIncomeStatement',		
                  'SLIncomeStatementSection',		
                  'SLIncomeStatementSequence',		
                  'SLBalanceSheetStatement', 		
                  'SLBalanceSheetStatementSection',		
                  'SLBalanceSheetStatementSequence',		
                  'SLCashFlowStatement',
                  'SLCashFlowStatementSection', 		
                  'SLCashFlowStatementSequence',		
                  'SLExpenseStatement',		
                  'SLExpenseStatementSection',		
                  'SLExpenseStatementSequence',		
                  'SLBudgetStatement',		
                  'SLBudgetStatementSection',		
                  'SLBudgetStatementSequence'		
	             )	
        widgets = {	
                    'SLStatementSectionFK': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLStatementLineFK': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLName': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLDescription': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLIncomeStatement': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLIncomeStatementSection': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLIncomeStatementSequence': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLBalanceSheetStatement': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLBalanceSheetStatementSection': forms.TextInput(attrs={ 		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLBalanceSheetStatementSequence': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLCashFlowStatement': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLCashFlowStatementSection': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLCashFlowStatementSequence': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLExpenseStatement': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLExpenseStatementSection': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLExpenseStatementSequence': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLBudgetStatement': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLBudgetStatementSection': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                    'SLBudgetStatementSequence': forms.TextInput(attrs={		
                    'class': INPUT_CLASSES	
                    }),	
                } 	

class StatementLineAccountsForm(forms.ModelForm):			
    class Meta:			
        model = StatementLineAccounts		
        fields = (			
         'SLAStatementSectionFK',			
         'SLAStatementLineFK',			
         'SLAStatementAccountFK',			
         'SAAccount',			
         'SLAAccountType',			
         'SLADescription',			
	          )		
    ordering = ['SAAccount']		
    widgets = {		
                'SLAStatementSectionFK': forms.TextInput(attrs={			
                'class': INPUT_CLASSES		
                }),		
                'SLAStatementLineFK': forms.TextInput(attrs={			
                'class': INPUT_CLASSES		
                }),		
                'SLAStatementAccountFK': forms.TextInput(attrs={			
                'class': INPUT_CLASSES		
                }),		
                'SAAccount': forms.TextInput(attrs={			
                'class': INPUT_CLASSES		
                }),		
                'SLAAccountType': forms.TextInput(attrs={			
                'class': INPUT_CLASSES		
                }),		
                'SLADescription': forms.TextInput(attrs={			
                'class': INPUT_CLASSES		
                }),		
                }		

class SectionSelectForm(forms.ModelForm):
    class Meta:
        model = StatementSections
        fields = ['SSName']

    SSName = forms.ModelChoiceField(queryset=StatementSections.objects.all(), widget=forms.Select(attrs={'class': INPUT_CLASSES}))