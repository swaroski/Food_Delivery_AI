from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from foodtaskerapp.models import Restaurant, Meal
#from foodtaskerapp.forms import UserForm, RestaurantForm

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")

class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("name", "phone", "address", "logo")

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude = ("restaurant",)
