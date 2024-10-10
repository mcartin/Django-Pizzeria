from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .models import *
from .forms import *

def index(request):
    return render(request, 'index.html')
def signup(request):
    if request.user.is_authenticated:
        return redirect('homePage.html')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('email')
                messages.success(request, 'Account was created for ' + user)
                return redirect('log_in')
        context = {'form':form}
        return render(request, 'signup.html', context)
def log_in(request):
    if request.user.is_authenticated:
        return redirect('homePage.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homePage.html')
            else:
                messages.info(request, 'Username OR password is incorrect')
                
        context = {}
        return render(request, 'log_in.html', context)
def logoutUser(request):
    logout(request)
    return redirect('log_in.html')
@login_required(login_url='log_in.html')
def homePage(request):
    return render(request, 'homePage.html')
@login_required(login_url='log_in.html')
def previous_orders(request):
    previous_pizzas = Pizza.objects.all()
    return render(request, 'previous_orders.html', {'previous_pizzas':previous_pizzas})
@login_required(login_url='log_in.html')
def create_pizzas(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            new_pizza = form.save()
            return render(request, 'created.html', {'pizza': new_pizza})
        else:
            return render(request, 'create_pizza.html', {'form':form})
    else:
    #     # its a GET request
    #     # load a new instance of the BookForm 
    #     # show it to the user
        form = PizzaForm()
        return render(request, 'create_pizza.html', {'form': form})
@login_required(login_url='log_in.html')
def created(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # If the form is valid, you can process the order
            # For now, let's just redirect to the confirmation page
            return redirect('confirmation.html')
    else:
        form = OrderForm()
    return render(request, 'created.html', {'form': form})

def confirmation(request):
    # Here you can provide the confirmation logic and render the confirmation page
    return render(request, 'confirmation.html')
