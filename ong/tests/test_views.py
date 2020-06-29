from django.test import TestCase, Client
from django.urls import reverse

from ong.models import User, Case


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home = reverse("home")
        self.user1 = User.objects.create(
            username="user1",
            password="password123",
            whatsapp="123456789",
            city="city",
            uf="TO",
        )
        self.case1 = Case.objects.create(
            title_case="case1", value=1000, status="ABERTO",
        )
        self.detail_url = reverse("detalhe", args=["1"])

    def test_indexpage_GET(self):

        response = self.client.get(self.home)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_detailpage_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "detail_case.html")
