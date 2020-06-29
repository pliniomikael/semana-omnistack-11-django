from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ong.views import (
    indexpage,
    detailpage,
    loginpage,
    painelpage,
    casosdelete,
    casosregistrarpage,
    registerpage,
    logoutpage,
    editcase,
)


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, indexpage)

    def test_login_url_is_resolved(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func, loginpage)

    def test_painel_url_is_resolved(self):
        url = reverse("painel")
        self.assertEquals(resolve(url).func, painelpage)

    def test_registrar_url_is_resolved(self):
        url = reverse("registrar")
        self.assertEquals(resolve(url).func, registerpage)

    def test_sair_url_is_resolved(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func, logoutpage)

    def test_detalhe_url_is_resolved(self):
        url = reverse("detalhe", args=["1"])
        self.assertEquals(resolve(url).func, detailpage)

    def test_caso_register_url_is_resolved(self):
        url = reverse("casosregistrarpage")
        self.assertEquals(resolve(url).func, casosregistrarpage)

    def test_caso_editar_url_is_resolved(self):
        url = reverse("editar", args=["1"])
        self.assertEquals(resolve(url).func, editcase)

    def test_caso_deletar_url_is_resolved(self):
        url = reverse("casosdelete", args=["1"])
        self.assertEquals(resolve(url).func, casosdelete)
