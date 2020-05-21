from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


# from django.contrib.auth.models import AbstractUser

from django import forms
from .models import *

# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "email",
            "first_name",
            "whatsapp",
            "city",
            "uf",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs = {"placeholder": "Nome da Ong", "required": True}
        self.fields["username"].widget.attrs = {"placeholder": "Usuário"}
        self.fields["password1"].widget.attrs = {"placeholder": "Senha"}
        self.fields["password2"].widget.attrs = {"placeholder": "Confirmar Senha"}
        self.fields["email"].widget.attrs = {"placeholder": "Email"}
        self.fields["whatsapp"].widget.attrs = {"placeholder": "Whatsapp"}
        self.fields["city"].widget.attrs = {"placeholder": "Cidade"}
        self.fields["uf"].widget.attrs = {"placeholder": "UF"}


class CreateCase(forms.ModelForm):
    class Meta:
        model = Case
        fields = ["title_case", "description", "value"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title_case"].widget.attrs["placeholder"] = "Titulo do Caso"
        self.fields["description"].widget.attrs = {"size": "40", "placeholder": "Descrição"}
        self.fields["value"].widget.attrs["placeholder"] = "Valor"


class EditCase(forms.ModelForm):
    class Meta:
        model = Case
        fields = ["title_case", "description", "value", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title_case"].widget.attrs["placeholder"] = "Titulo do Caso"
        self.fields["description"].widget.attrs = {"size": "40", "placeholder": "Descrição"}
        self.fields["value"].widget.attrs["placeholder"] = "Valor"
        self.fields["status"].widget.attrs = {"placeholder": "Status"}
