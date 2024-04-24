from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Item

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')  # Redirect to index page upon successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def index(request):
    if request.user.is_authenticated:  # Check if user is logged in
        user_items = Item.objects.filter(user=request.user)  # Get items associated with the current user
        return render(request, 'index.html', {'user_items': user_items})
    else:
        return redirect('login')  # Redirect to login page if user is not authenticated
