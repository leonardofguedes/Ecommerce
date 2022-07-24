from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Seu nome completo"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite seu email",
            }
        )
    )
    mensagem = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua mensagem",
            }
        )
    )