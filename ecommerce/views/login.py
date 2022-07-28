from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ecommerce.forms.login_form import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print('Login Inválido')
    return render(request, "pages/login.html", context)