from django.shortcuts import render


def about(request):
    return render(request, 'pages/about.html', context={
        "title": "Sobre",
        "content": "Esse é um site de vendas",
    })
