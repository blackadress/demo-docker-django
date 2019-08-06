from django.urls import reverse, resolve

class TestUrls:
    
    def test_inicio_url(self):
        path = reverse('saludo:inicio')
        assert resolve(path).view_name == 'saludo:inicio'
    
    def test_login_url(self):
        path = reverse('saludo:login')
        assert resolve(path).view_name == 'saludo:login'

    def test_logout_url(self):
        path = reverse('saludo:logout')
        assert resolve(path).view_name == 'saludo:logout'
    
    def test_registrar_url(self):
        path = reverse('saludo:registrar')
        assert resolve(path).view_name == 'saludo:registrar'