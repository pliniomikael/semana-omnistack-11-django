from django.urls import path

from . import views

urlpatterns = [
    path("", views.indexpage, name="home"),
    path("login/", views.loginpage, name="login"),
    path("painel/", views.painelpage, name="painel"),
    path("detalhe/<int:pk>", views.detailpage, name="detalhe"),
    path("casos/registrar/", views.casosregistrarpage, name="casosregistrarpage"),
    path("casos/editar/<int:pk>/", views.editcase, name="editar"),
    path("casos/delete/<int:pk>/", views.casosdelete, name="casosdelete"),
    path("registrar/", views.registerpage, name="registrar"),
    path("sair/", views.logoutpage, name="logout"),
]
