from django import forms
from django.contrib.auth import password_validation, authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from accounts.models import User


# class RegisterForm(UserCreationForm):
#     password1 = forms.CharField(
#         label="Password",
#         strip=False,
#         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mb-3 w-50'}),
#         help_text=password_validation.password_validators_help_text_html(),
#     )
#     password2 = forms.CharField(
#         label="Password confirmation",
#         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mb-3 w-50'}),
#         strip=False,
#         help_text="Enter the same password as before, for verification.",
#     )
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = [
#             'role', 'username', 'email', 'password1', 'password2',
#             'phone', 'photo'
#         ]
#
#         widgets = {
#             'role': forms.Select(attrs={'class': 'form-control mb-3 w-50'}),
#             'username': forms.TextInput(attrs={'class': 'form-control mb-3 w-50'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control mb-3 w-50', 'required': True}),
#             'phone': forms.NumberInput(attrs={'class': 'form-control mb-3 w-50'}),
#             'photo': forms.FileInput(attrs={'class': 'form-control mb-3 w-50'})
#         }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=254, label='Username',
                                        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))


# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'photo']
#         labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Почта'}
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control mb-3'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
#             'phone': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
#             'photo': forms.FileInput(attrs={'class': 'form-control mb-3 w-50'})
#         }

