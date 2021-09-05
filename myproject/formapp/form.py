from django import forms
from django.forms import ModelForm
from formapp.models import Register

class Reg(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['names','mobile_no','age','gender','branch']
        widgets={
            'names': forms.TextInput(attrs={'class':'from-control','placeholder':'Enter your name'}),
            'mobile_no': forms.TextInput(attrs={'class':'from-control','placeholder':'Enter your mobile number'}),
            'age': forms.NumberInput(attrs={'class':'from-control','placeholder':'Enter your age'}),
            'gender': forms.RadioSelect(attrs={'type':'radio','placeholder':'Enter your gender'}),
            'branch': forms.Select(attrs={'class':'from-control'}),
        }