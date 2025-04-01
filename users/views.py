from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'html/users/register.html', {'form': form,'error': 'Invalid form submission'})
    else:
        form = UserCreationForm()
        return render(request, 'html/users/register.html', {'form': form})
    
def user_logout(request):
    logout(request)
    return redirect('login')
