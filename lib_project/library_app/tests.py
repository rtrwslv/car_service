from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
import pytest

@pytest.mark.django_db
def test_get_books():
    client = APIClient()
    user = get_user_model().objects.create_user(username='test', password='test')
    client.force_authenticate(user=user)
    response = client.get('/api/books/')
    assert response.status_code == status.HTTP_200_OK
