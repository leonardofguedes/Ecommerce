from unittest import TestCase
from ecommerce.forms.contact_form import ContactForm
from parameterized import parameterized


class ContactFormUnitTest(TestCase):
    @parameterized.expand([
        ('nome', 'Seu nome completo'),
        ('email', 'Digite seu email'),
        ('mensagem', 'Digite sua mensagem'),
    ])
    def test_fields_placeholder(self, field, placeholder):
        form = ContactForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)