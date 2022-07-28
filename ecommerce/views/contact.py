from django.shortcuts import render
from ecommerce.forms.contact_form import ContactForm


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