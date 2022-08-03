from unittest import TestCase
from ecommerce.forms.contact_form import ContactForm
from ecommerce.forms.register_form import RegisterForm
from ecommerce.forms.login_form import LoginForm
from ecommerce.forms.addresses_form import AddressForm
from parameterized import parameterized


class ContactFormUnitTest(TestCase):
    @parameterized.expand([
            ('nome', {'required': 'Obrigatório o preenchimento do nome'}),
            ('email', {'invalid': 'Digite um email válido!', 'required': 'This field is required.'}),
            ('mensagem', {'required': 'É obrigatório o preenchimento do campo mensagem!'}), ])
    def test_fields_error_messages(self, field, needed):
        form = ContactForm()
        current = form[field].field.error_messages
        self.assertEqual(current, needed)


class RegisterFormUniTest(TestCase):
    @parameterized.expand([
        ('password', {'required': 'This field is required.'}),
        ('username', {'required': 'This field is required.'}),
        ('password2', {'required': 'This field is required.'}),
        ('email', {'required': 'This field is required.'}), ])
    def test_fields_error_messages(self, field, needed):
        form = RegisterForm()
        current = form[field].field.error_messages
        self.assertEqual(current, needed)


class LoginFormUniTest(TestCase):
    @parameterized.expand([
        ('password', {'required': 'This field is required.'}),
        ('username', {'required': 'This field is required.'}),])
    def test_fields_error_messages(self, field, needed):
        form = LoginForm()
        current = form[field].field.error_messages
        self.assertEqual(current, needed)


class AddressFormUniTest(TestCase):
    @parameterized.expand([
        ('address_line_1', {'required': 'This field is required.'}),
        ('address_line_2', {'required': 'This field is required.'}),
        ('city', {'required': 'This field is required.'}),
        ('state', {'required': 'This field is required.'}),
        ('postal_code', {'required': 'This field is required.'}), ])
    def test_fields_error_messages(self, field, needed):
        form = AddressForm()
        current = form[field].field.error_messages
        self.assertEqual(current, needed)