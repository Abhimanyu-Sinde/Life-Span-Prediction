from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Home(forms.Form):
    Year = forms.IntegerField()
    Status=forms.IntegerField()
    Adult_Mortality = forms.IntegerField()
    Infant_deaths = forms.IntegerField()
    Alcohol = forms.FloatField()
    Expenditure= forms.FloatField()
    Hepatitis_b=forms.IntegerField()
    Measles = forms.IntegerField()
    BMI = forms.FloatField()
    Under_five_deaths = forms.IntegerField()
    Polio = forms.IntegerField()
    Total_expenditure = forms.FloatField()
    Diphtheria = forms.IntegerField()
    HIV_AIDS = forms.FloatField()
    GDP = forms.FloatField()
    Population = forms.IntegerField()
    Thinness_19_years = forms.FloatField()
    Thinness_9_years = forms.FloatField()
    Income_Composition = forms.FloatField()
    Schooling = forms.FloatField()

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1','password2']