from unittest import TestCase
from ecommerce.forms.contact_form import ContactForm
from parameterized import parameterized


class ContactFormUnitTest(TestCase):
    @parameterized.expand([
            ('nome', {'required': 'Obrigatório o preenchimento do nome'}),
            ('email', {'invalid': 'Digite um email válido!', 'required': 'This field is required.'}),
            ('mensagem', {'required':'É obrigatório o preenchimento do campo mensagem!'}),])
    def test_fields_help_text(self, field, needed):
        form = ContactForm()
        current = form[field].field.error_messages
        self.assertEqual(current, needed)