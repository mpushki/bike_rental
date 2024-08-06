import pytest

from django.urls import reverse

import pytest


@pytest.mark.django_db
def test_user_create(client):
   data = {'password': 'someone', 'name': 'Some User', 'email':'someone@gmail.com'}
   url = reverse('sign_up')
   response = client.post(url, data, format='json')
   assert response.status_code == 201
   assert 'someone@gmail.com' == response.data.get('email')
