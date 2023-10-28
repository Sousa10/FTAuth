from django import forms
from django.forms import ModelForm
from .models import workout, ExcerciseList

# Create a Workout Form
class WorkoutForm(ModelForm):
    class Meta:
        model = workout
        # fields = ('DetailID', 'WorkoutID', 'ExcerID', 'Region', 'Area', 'Exercise', 'SetOneReps', 'SetOneWeight', 'SetTwoReps', 'SetTwoWeight', 'SetThreeReps', 'SetThreeWeight', 'SetFourReps', 'SetFourWeight')
        fields = ('WorkoutName', 'Region', 'Area', 'Exercise', 'SetOneReps', 'SetOneWeight', 'SetTwoReps', 'SetTwoWeight', 'SetThreeReps', 'SetThreeWeight', 'SetFourReps', 'SetFourWeight')
        labels = {
            'WorkoutName': '',
            'Region': '',
            'Area': '',
            'Exercise': '',
            'SetOneReps': '',
            'SetOneWeight': '',
            'SetTwoReps': '',
            'SetTwoWeight': '',
            'SetThreeReps': '',
            'SetThreeWeight': '',
            'SetFourReps': '',
            'SetFourWeight': '',
        }
        widgets = {
            'WorkoutName': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'Region': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Region'}),
            'Area': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Area'}),
            'Exercise': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Excercise'}),
            'SetOneReps': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'#1 Reps'}),
            'SetOneWeight': forms.TextInput(attrs={'class':'form-control', 'placeholder':'#1 Weight'}),
            'SetTwoReps': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'#2 Reps'}),
            'SetTwoWeight': forms.TextInput(attrs={'class':'form-control', 'placeholder':'#2 Weight'}),
            'SetThreeReps': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'#3 Reps'}),
            'SetThreeWeight': forms.TextInput(attrs={'class':'form-control', 'placeholder':'#3 Weight'}),
            'SetFourReps': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'#4 Reps'}),
            'SetFourWeight': forms.TextInput(attrs={'class':'form-control', 'placeholder':'#4 Weight'}),
        }

# Create an Excercise Form
class ExcerciseForm(ModelForm):
    class Meta:
        model = ExcerciseList
        fields = ('Reference', 'Region', 'Area', 'Exercise', 'Description', 'Instructions')
        labels = {
            'Reference': '',
            'Region': '',
            'Area': '',
            'Exercise': '',
            'Description': '',
            'Instructions': '',
        }
        widgets = {
            'Reference': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Reference'}),
            'Region': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Region'}),
            'Area': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Area'}),
            'Exercise': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Excercise'}),
            'Description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
            'Instructions': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Instructions'}),
        }
