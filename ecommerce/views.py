from django.shortcuts import render, redirect
from .forms.contact_form import ContactForm
from django.contrib.auth import authenticate, login, get_user_model
from .forms.login_form import LoginForm
from .forms.register_form import RegisterForm


def home_page(request):
    context = {"title": "Home Page", "content":"Bem-vindo a Home Page"}
    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
        return render(request, 'pages/home.html', context)
    return render(request, 'pages/home.html', context)


def about(request):
    return render(request, 'pages/about.html', context={
        "title": "Sobre",
        "content": "Esse é um site de vendas",
    })


def contact(request):
    contact_form = ContactForm(request.POST or None)
    if request.method == "POST":
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
    return render(request, 'pages/contact.html', context = {
        "title": "Contatos",
        "content": "Bem-vindo a página de contato",
        "form": contact_form,
    })


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


def register_page(request):
    User = get_user_model()
    form = RegisterForm(request.POST or None)
    context = {
                    "form": form
              }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "pages/register.html", context)