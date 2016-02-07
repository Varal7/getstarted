from .models import Participant
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import filesizeformat



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('username', 'first_name', 'last_name',  'email', 'promo', 'cv', 'year_in_school', 'found_stage', 'domains', 'missions', 'want_cocktail')
        widgets = {
            'username': forms.HiddenInput(),
            'promo' : forms.HiddenInput(),
            'first_name': forms.TextInput(attrs={'readonly':'readonly','class':'form-control'}),
            'last_name': forms.TextInput(attrs={'readonly':'readonly','class':'form-control'}),
            'email': forms.TextInput(attrs={'readonly':'readonly','class':'form-control'}),
            'cv' : forms.FileInput(attrs={'class':'form-control'}),
            'year_in_school' : forms.Select(attrs={'class':'form-control'}),
            'found_stage' : forms.Select(attrs={'class':'form-control'}),
            'want_cocktail' : forms.Select(attrs={'class':'form-control'}),
            'domains' : forms.Textarea(attrs={'class':'form-control', 'rows':4}),
            'missions' : forms.Textarea(attrs={'class':'form-control', 'rows':4}),
        }
    def clean_cv(self):
        cv = self.cleaned_data['cv']
        if cv is not None:
            content_type = cv.content_type
            if content_type in settings.CONTENT_TYPES:
                if cv._size > settings.MAX_UPLOAD_SIZE:
                    raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(cv._size)))
            else:
                raise forms.ValidationError(_('File type is not supported'))
        return cv



class UpdateCvForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('cv',)
        widgets = {
            'cv' : forms.FileInput(attrs={'class':'form-control'}),
        }
    def clean_cv(self):
        cv = self.cleaned_data['cv']
        content_type = cv.content_type
        if content_type in settings.CONTENT_TYPES:
            if cv._size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(cv._size)))
        else:
            raise forms.ValidationError(_('File type is not supported'))
        return cv
