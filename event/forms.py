from .models import Participant
from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('username', 'first_name', 'last_name',  'email', 'promo', 'cv',  'year_in_school', 'found_stage', 'domains', 'missions')
        widgets = {
            'found_stage': forms.RadioSelect,
            'username': forms.HiddenInput(),
            'promo' : forms.HiddenInput(),
            'first_name': forms.TextInput(attrs={'readonly':'readonly'}),
            'last_name': forms.TextInput(attrs={'readonly':'readonly'}),
            'email': forms.TextInput(attrs={'readonly':'readonly'}),
        }
