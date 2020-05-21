from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.db.models import Sum


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .models import *
from .decorators import *
from .forms import *


def indexpage(request):
    todos = Case.objects.filter(status="ABERTO").order_by("-datahora")
    total = Case.objects.filter(status="ABERTO").count()

    context = {"todos": todos, "total": total}
    return render(request, "home.html", context)


@unauthenticated_user
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("painel")
        else:
            messages.info(request, "Usuario ou Senha Invalida!")

    context = {}
    return render(request, "login.html", context)


@login_required(login_url="login")
def painelpage(request):
    caso = Case.objects.filter(ong_name=request.user).order_by("-datahora")
    caso_aberto = Case.objects.filter(ong_name=request.user, status="ABERTO").count()
    caso_finalizado = Case.objects.filter(ong_name=request.user, status="FINALIZADO").count()
    valor_total_aberto = Case.objects.filter(ong_name=request.user, status="ABERTO").aggregate(
        Sum("value")
    )
    valor_total_finalizado = Case.objects.filter(
        ong_name=request.user, status="FINALIZADO"
    ).aggregate(Sum("value"))
    context = {
        "caso": caso,
        "caso_aberto": caso_aberto,
        "caso_finalizado": caso_finalizado,
        "valor_total_aberto": valor_total_aberto,
        "valor_total_finalizado": valor_total_finalizado,
    }
    return render(request, "painel.html", context)


@login_required(login_url="login")
def casosdelete(request, pk):
    deletar = Case.objects.get(id=pk)
    if request.method == "POST":  # If method is POST,
        deletar.delete()  # delete the cat.
        return redirect("painel")
    context = {}
    return redirect("painel")


@login_required(login_url="login")
def casosregistrarpage(request):
    if request.method == "POST":
        formcasos = CreateCase(request.POST)
        if formcasos.is_valid():
            case = formcasos.save(commit=False)
            case.ong_name = request.user
            case.save()
            return redirect("painel")
    else:
        formcasos = CreateCase()
    context = {"formcasos": formcasos}

    return render(request, "register_case.html", context)


def registerpage(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            regi = form.save(commit=False)
            form.save()
            return redirect("home")
    else:
        form = CreateUserForm()
    context = {"form": form}
    return render(request, "register.html", context)


def logoutpage(request):
    logout(request)
    return redirect("home")


@login_required(login_url="login")
def editcase(request, pk):
    caso = Case.objects.get(id=pk)
    if request.method == "POST":
        formcasos = CreateCase(request.POST, instance=caso)
        if formcasos.is_valid():
            case = formcasos.save(commit=False)
            case.ong_name = request.user
            case.save()
            return redirect("painel")
    else:
        formcasos = CreateCase(instance=caso)
    context = {"formcasos": formcasos}
    return render(request, "edit_case.html", context)


def detailpage(request, pk):
    caso = Case.objects.get(id=pk)
    context = {"caso": caso}
    return render(request, "detail_case.html", context)
