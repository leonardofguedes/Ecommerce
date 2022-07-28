from django.shortcuts import render
from django.contrib.auth import get_user_model
from ecommerce.forms.register_form import RegisterForm


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