from django import forms
from .models import MedicalRecord

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'diagnosis', 'prescription', 'notes', 'report_file']
        widgets = {
            'patient': forms.Select(attrs={
                'class': 'form-control'
            }),
            'diagnosis': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter diagnosis'
            }),
            'prescription': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter prescribed medicines',
                'rows': 3
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional notes',
                'rows': 3
            }),
            'report_file': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }
