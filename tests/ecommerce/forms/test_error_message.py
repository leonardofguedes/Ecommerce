from unittest import TestCase
from ecommerce.forms.contact_form import ContactForm
from ecommerce.forms.register_form import RegisterForm
from parameterized import parameterized


class ContactFormUnitTest(TestCase):
    @parameterized.expand([
            ('nome', {'required': 'Obrigatório o preenchimento do nome'}),
            ('email', {'invalid': 'Digite um email válido!', 'required': 'This field is required.'}),
            ('mensagem', {'required': 'É obrigatório o preenchimento do campo mensagem!'}), ])
    def test_fields_help_text(self, field, needed):
        form = ContactForm()
        current = form[field].field.error_messages
        self.assertEqual(current, needed)


class RegisterFormUniTest(TestCase):
    @parameterized.expand([
        ('password', {'required': 'This field is required.'}), ])
    def test_fields_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.error_messages
        self.assertEqual(current, needed)
