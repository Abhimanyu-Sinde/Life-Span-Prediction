from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .forms import CreateUserForm
from django.contrib import messages
from .forms import Home
#from Life_util import pred

def home(request):
    form=Home()
    context = {'form':form}
    return render(request, 'home.html', context)

def result(request):
    if(request.method=='POST'):
        Year = request.POST['Year']
        Status= request.POST['Status']
        Adult_Mortality = request.POST['Adult_Mortality']
        Infant_deaths = request.POST['Infant_deaths']
        Alcohol = request.POST['Alcohol']
        Expenditure= request.POST['Expenditure']
        Hepatitis_b=request.POST['Hepatitis_b']
        Measles = request.POST['Measles']
        BMI = request.POST['BMI']
        Under_five_deaths = request.POST['Under_five_deaths']
        Polio = request.POST['Polio']
        Total_expenditure = request.POST['Total_expenditure']
        Diphtheria = request.POST['Diphtheria']
        HIV_AIDS = request.POST['HIV_AIDS']
        GDP = request.POST['GDP']
        Population = request.POST['Population']
        Thinness_19_years = request.POST['Thinness_19_years']
        Thinness_9_years = request.POST['Thinness_9_years']
        Income_Composition = request.POST['Income_Composition']
        Schooling = request.POST['Schooling']

    result = predict(Year, Status, Adult_Mortality, Infant_deaths, Alcohol, Expenditure, Hepatitis_b,
                             Measles, BMI, Under_five_deaths, Polio, Total_expenditure, Diphtheria, 
                             HIV_AIDS, GDP, Population, Thinness_19_years, Thinness_9_years,
                              Income_Composition, Schooling)

    return render(request, 'result.html', {'result':result})

def predict(Year, Status, Adult_Mortality, Infant_deaths, Alcohol, Expenditure, Hepatitis_b, Measles, BMI, 
            Under_five_deaths, Polio, Total_expenditure, Diphtheria, HIV_AIDS, GDP, Population,
             Thinness_19_years, Thinness_9_years, Income_Composition, Schooling):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    import os
    cur_path = os.path.dirname(__file__)
    path = os.path.join(cur_path,"Life Expectancy Data.csv")
    df= pd.read_csv(path)

    df.isnull().any().sum()

    df.fillna(method='bfill',inplace=True)
    df.isnull().any().sum()

    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()  
    df['Status'] = le.fit_transform(df['Status'])

    X=df.drop(columns=['Country','Life expectancy '])
    y=df['Life expectancy ']

    from sklearn.model_selection import train_test_split

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

    #Random Forest Reggression

    from sklearn.ensemble import RandomForestRegressor
    model=RandomForestRegressor()

    #training the model
    model.fit(X_train,y_train)

    y_pred=model.predict(X_test)

    x=[[Year, Status, Adult_Mortality, Infant_deaths, Alcohol, Expenditure, Hepatitis_b, Measles, BMI, 
            Under_five_deaths, Polio, Total_expenditure, Diphtheria, HIV_AIDS, GDP, Population,
             Thinness_19_years, Thinness_9_years, Income_Composition, Schooling]]

    y=model.predict(x)
    
    
    return y[0]


def Register(request):
      form = CreateUserForm()

      if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                  form.save()
                  first = form.cleaned_data.get('first_name')
                  last = form.cleaned_data.get('last_name')
                  
                  messages.success(request, 'Account was successfully created for ' + first + last)

                  return redirect('login')


      context = {'form': form}
      return render(request, 'life1.html', context)

def Login(request):

      if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                  login(request, user)
                  return redirect('/')

            else:
                  messages.info(request, 'Username or Password is incorrect')
      context = {}
      return render(request, 'life1.html', context)


def logoutUser(request):
      logout(request)
      return redirect('/')