from django.shortcuts import render


def home_page(request):
    context = {"title": "Home Page", "content":"Bem-vindo a Home Page"}
    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
        return render(request, 'pages/home.html', context)
    return render(request, 'pages/home.html', context)