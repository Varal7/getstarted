from .models import Participant
from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('username', 'first_name', 'last_name',  'email', 'promo', 'cv',  'year_in_school', 'found_stage', 'domains', 'missions')
        widgets = {
            'username': forms.HiddenInput(),
            'promo' : forms.HiddenInput(),
            'first_name': forms.TextInput(attrs={'readonly':'readonly','class':'form-control'}),
            'last_name': forms.TextInput(attrs={'readonly':'readonly','class':'form-control'}),
            'email': forms.TextInput(attrs={'readonly':'readonly','class':'form-control'}),
            'cv' : forms.FileInput(attrs={'class':'form-control'}),
            'year_in_school' : forms.Select(attrs={'class':'form-control'}),
            'found_stage' : forms.Select(attrs={'class':'form-control'}),
            'domains' : forms.Textarea(attrs={'class':'form-control', 'rows':4}),
            'missions' : forms.Textarea(attrs={'class':'form-control', 'rows':4}),
        }
