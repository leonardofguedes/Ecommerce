from django.test import TestCase as DjangoTestCase
from django.urls import reverse


class ContactFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'nome': 'user test django',
            'mensagem': 'mensagem teste',
            'email': 'email.anyemail.com',
        }
        return super().setUp(*args, **kwargs)


    def test_field_email_invalid(self):
        msg = 'Digite um email válido!'
        url = reverse('contact')
        response = self.client.post(url, data=self.form_data, follow=True)
        print(response.content.decode('utf-8'))
        self.assertIn(msg, response.content.decode('utf-8'))