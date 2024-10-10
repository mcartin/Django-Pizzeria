from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 'toppings']

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=200)
    card_number = forms.CharField(max_length=16)
    card_expiry_month = forms.IntegerField(min_value=1, max_value=12)
    card_expiry_year = forms.IntegerField(min_value=2022, max_value=2050)
    card_cvv = forms.CharField(max_length=4)

