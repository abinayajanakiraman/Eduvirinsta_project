from django import forms
from .models import *

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class schoolAdmin(forms.ModelForm):
    class Meta:
        model= School_Admin
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'school':forms.TextInput(attrs={'class':'form-control'}),
            'Regno':forms.TextInput(attrs={'class':'form-control'}),
        }

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields=['name','password','stand','Regno']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'stand':forms.TextInput(attrs={'class':'form-control'}),
            'Regno':forms.TextInput(attrs={'class':'form-control'}),
        }

class studentform2(forms.ModelForm):
    class Meta:
        model=student
        fields=['tamil','science','Maths','Social','English','Regno']
        widgets={
            'tamil':forms.TextInput(attrs={'class':'form-control'}),
            'science':forms.TextInput(attrs={'class':'form-control'}),
            'Maths':forms.TextInput(attrs={'class':'form-control'}),
            'Social':forms.TextInput(attrs={'class':'form-control'}),
            'English':forms.TextInput(attrs={'class':'form-control'}),
        }

class stafform(forms.ModelForm):
    class Meta:
        model=staff
        fields=['name','password','stand','Regno','subj']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'stand':forms.TextInput(attrs={'class':'form-control'}),
            'Regno':forms.TextInput(attrs={'class':'form-control'}),
            'subj':forms.TextInput(attrs={'class':'form-control'}),
        }

