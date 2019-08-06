from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser

from mixer.backend.django import mixer
import pytest

from saludo.views import InicioView, LoginView, LogoutView, SignUp

def setup_view(view, *args, **kwargs):
    view.args = args
    view.kwargs = kwargs
    return view

@pytest.mark.django_db
class TestViews:
    
    def test_inicio_view_get(self):
        path = reverse('saludo:inicio')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        v = setup_view(InicioView())

        response = v.get(request)
        assert response.status_code == 200

    def test_login_view_get(self):
        path = reverse('saludo:login')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()
        v = setup_view(LoginView())
        print(request)

        response = v.get(request)
        assert response.status_code == 200

    # def test_logout_view_get(self):
    #     path = reverse('saludo:logout')
    #     request = RequestFactory().get(path)
    #     request.user = mixer.blend(User)
    #     v = setup_view(LogoutView())

    #     response = v.get(request)
    #     assert response.status_code == 302

    def test_signup_view_test(self):
        path = reverse('saludo:registrar')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()
        v = setup_view(SignUp())

        response = v.get(request)
        assert response.status_code == 200


