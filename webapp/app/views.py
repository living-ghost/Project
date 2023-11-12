from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import RegistrationForm, LoginForm

def index(request):
    return render(request, 'index.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            
            # Authenticate manually
            user = UserProfile.objects.filter(username=username, password1=password1).first()
            
            if user is not None:
                return redirect('index')
            else:
                # Handle invalid login credentials
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'sign_in.html', {'form': form})