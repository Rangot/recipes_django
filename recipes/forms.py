from django import forms
from .models import *


class DeviceFirmwareForm(forms.ModelForm):
    class Meta:
        model = DeviceFirmware
        fields = ['major_version', 'minor_version', 'device_id', 'hidden_flag', 'tag', 'en', 'ru']

        widgets = {
            'major_version': forms.NumberInput(attrs={'class': 'form-control'}),
            'minor_version': forms.NumberInput(attrs={'class': 'form-control'}),
            'device_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'hidden_flag': forms.NumberInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'en': forms.Textarea(attrs={'class': 'form-control'}),
            'ru': forms.Textarea(attrs={'class': 'form-control'})
        }


class ImageVariantsForm(forms.ModelForm):
    class Meta:
        model = ImageVariants
        fields = ['image_id', 'language_id', 'value']

        widgets = {
            'image_id': forms.Select(attrs={'class': 'form-control'}),
            'language_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'value': forms.TextInput(attrs={'class': 'form-control'})
        }

