from django.shortcuts import render, redirect
from django.views import View
from .forms import SignupForm
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Profile

# Create your views here.


class SignupView(View):
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not Profile.objects.filter(user=user).exists():
                Profile.objects.create(user=user)
            return redirect('all-products')
        else:
            return render(request, 'accounts/signup.html', {'form': form})

    def get(self, request):
        form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})


class LoginView(View):
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('all-products')
        return render(request, 'accounts/login.html', {'form': form})

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

