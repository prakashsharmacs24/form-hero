from django.contrib.auth import get_user_model
from formhero.apps.models import App
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from formhero.forms.views import CreateForm
from rest_framework import status


User = get_user_model()


class RetrievePostFormTests(APITestCase):

    def test_post_a_new_form(self):
        app1 = App.objects.create(host_list=["testserver"])
        handler = 'db'
        data = {"app": app1.pk, "name": "Szymon", "handler": handler, "config": "test"}
        url = reverse(CreateForm.URL_NAME, kwargs={'pk': app1.pk})
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['app'], app1.pk)
        self.assertEqual(response.data['name'], "Szymon")
        self.assertEqual(response.data['handler'], handler)
        self.assertEqual(response.data['config'], "test")

    def test_should_not_allow_to_post(self):
        app1 = App.objects.create()
        handler = 'db'
        data = {"app": app1.pk, "name": "Szymon", "handler": handler, "config": "test"}
        url = reverse(CreateForm.URL_NAME, kwargs={'pk': app1.pk})
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
