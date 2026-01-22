from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import User, Profile

class RegisterForm(UserCreationForm):
    Role_Choices = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('receptionist', 'Receptionist'),
        ('patient', 'Patient'),
    )
    username = forms.CharField(max_length=100, label='Full-Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    role = forms.CharField(label='Select-Role', widget=forms.Select(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm-Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if email and password:
            try:
                user = User.objects.get(email=email)
                self.cleaned_data['username'] = user.username

            except User.DoesNotExist:
                raise forms.ValidationError("Invalid Email or Password")
            
        return super().clean()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'created_at']
        widgets = {
            'patient_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'hospital_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hospital name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your address', 'rows': 3}),
            'blood_group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blood group (e.g., A+)'}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        }
