from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

def register_page(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
        return redirect(reverse_lazy('login-page'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'login/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    next_page = reverse_lazy('main-page')