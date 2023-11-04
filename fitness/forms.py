from django import forms
from django.forms import ModelForm
from .models import workout, ExcerciseList, training_routine, golf_course

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
            'Description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description', "rows": 3}),
            'Instructions': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Instructions', "rows": 3}),
        }

# Create an Routine Form
class RoutineForm(ModelForm):
    class Meta:
        model = training_routine
        fields = ('RoutineName', 'Description', 'Benefits', 'Instructions', 'ResultsComments')
        labels = {
            'RoutineName': '',
            'Description': '',
            'Benefits': '',
            'Instructions': '',
            'ResultsComments': '',
        }
        widgets = {
            'RoutineName': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Routnine'}),
            'Description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Desciption'}),
            'Benefits': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Benefits'}),
            'Instructions': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Instructions', "rows": 3}),
            'ResultsComments': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Results & Comments'}),
        }

# Create an Golf Course Form
class GolfCourseForm(ModelForm):
    class Meta:
        model = golf_course
        fields = ('Course', 'CoursePar', 'Yards', 'Slope', 'Rating', 'Description',
                  'Hole1Par', 'Hole1Yardage', 'Hole1Handicap', 'Hole2Par', 'Hole2Yardage', 'Hole2Handicap',
                  'Hole3Par', 'Hole3Yardage', 'Hole3Handicap', 'Hole4Par', 'Hole4Yardage', 'Hole4Handicap',
                  'Hole5Par', 'Hole5Yardage', 'Hole5Handicap', 'Hole6Par', 'Hole6Yardage', 'Hole6Handicap',
                  'Hole7Par', 'Hole7Yardage', 'Hole7Handicap', 'Hole8Par', 'Hole8Yardage', 'Hole8Handicap',
                  'Hole9Par', 'Hole9Yardage', 'Hole9Handicap', 'Hole10Par', 'Hole10Yardage', 'Hole10Handicap',
                  'Hole11Par', 'Hole11Yardage', 'Hole11Handicap', 'Hole12Par', 'Hole12Yardage', 'Hole12Handicap',
                  'Hole13Par', 'Hole13Yardage', 'Hole13Handicap', 'Hole14Par', 'Hole14Yardage', 'Hole14Handicap',
                  'Hole15Par', 'Hole15Yardage', 'Hole15Handicap', 'Hole16Par', 'Hole16Yardage', 'Hole16Handicap',
                  'Hole17Par', 'Hole17Yardage', 'Hole17Handicap', 'Hole18Par', 'Hole18Yardage', 'Hole18Handicap',)
        labels = {
            'Course': '',
            'CoursePar': '',
            'Yards': '',
            'Slope': '',
            'Rating': '',
            'Description': '',
            'Hole1Par': '',
            'Hole1Yardage': '',
            'Hole1Handicap': '',
            'Hole2Par': '',
            'Hole2Yardage': '',
            'Hole2Handicap': '',
            'Hole3Par': '',
            'Hole3Yardage': '',
            'Hole3Handicap': '',
            'Hole4Par': '',
            'Hole4Yardage': '',
            'Hole4Handicap': '',
            'Hole5Par': '',
            'Hole5Yardage': '',
            'Hole5Handicap': '',
            'Hole6Par': '',
            'Hole6Yardage': '',
            'Hole6Handicap': '',
            'Hole7Par': '',
            'Hole7Yardage': '',
            'Hole7Handicap': '',
            'Hole8Par': '',
            'Hole8Yardage': '',
            'Hole8Handicap': '',
            'Hole9Par': '',
            'Hole9Yardage': '',
            'Hole9Handicap': '',
            'Hole10Par': '',
            'Hole10Yardage': '',
            'Hole10Handicap': '',
            'Hole11Par': '',
            'Hole11Yardage': '',
            'Hole11Handicap': '',
            'Hole12Par': '',
            'Hole12Yardage': '',
            'Hole12Handicap': '',
            'Hole13Par': '',
            'Hole13Yardage': '',
            'Hole13Handicap': '',
            'Hole14Par': '',
            'Hole14Yardage': '',
            'Hole14Handicap': '',
            'Hole15Par': '',
            'Hole15Yardage': '',
            'Hole15Handicap': '',
            'Hole16Par': '',
            'Hole16Yardage': '',
            'Hole16Handicap': '',
            'Hole17Par': '',
            'Hole17Yardage': '',
            'Hole17Handicap': '',
            'Hole18Par': '',
            'Hole18Yardage': '',
            'Hole18Handicap': '',
        }
        widgets = {
            'Course': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Course', 'size': '20'}),
            'CoursePar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Par'}),
            'Yards': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Slope': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Slope'}),
            'Rating': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Rating'}),
            'Description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
            'Hole1Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole1'}),
            'Hole1Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole1Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole2Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole2'}),
            'Hole2Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole2Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole3Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole3'}),
            'Hole3Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole3Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole4Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole4'}),
            'Hole4Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole4Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole5Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole5'}),
            'Hole5Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole5Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole6Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole6'}),
            'Hole6Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Yds'}),
            'Hole6Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole7Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole7'}),
            'Hole7Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole7Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole8Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole8'}),
            'Hole8Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole8Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole9Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole9'}),
            'Hole9Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole9Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole10Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole10'}),
            'Hole10Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole10Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole11Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole11'}),
            'Hole11Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole11Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole12Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole12'}),
            'Hole12Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole12Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole13Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole13'}),
            'Hole13Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole13Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole14Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole14'}),
            'Hole14Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole14Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole15Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole15'}),
            'Hole15Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole15Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole16Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole16'}),
            'Hole16Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole16Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole17Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole17'}),
            'Hole17Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole17Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
            'Hole18Par': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hole18'}),
            'Hole18Yardage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YDs'}),
            'Hole18Handicap': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hcp'}),
        }        