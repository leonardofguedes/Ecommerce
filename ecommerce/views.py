from django.http import HttpResponse
from django.shortcuts import render
from .forms.contact_form import ContactForm

def home_page(request):
    return render(request, 'pages/home.html', context={
        "title": 'Página Principal',
        "content": 'Bem-vindo a página principal'
    })

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