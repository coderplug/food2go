from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    email = forms.CharField(max_length=254, help_text="You’ll need access to this email address to verify your account and get sweet deals.")
    phone_number = forms.CharField(max_length=22, help_text="This is required for our delivery guy to contact you.")
    delivery_address = forms.CharField(max_length=200, help_text="Your order needs to go somewhere.")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_address', 'password1', 'password2', )