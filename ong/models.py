from django.db import models
from datetime import datetime
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth.models import AbstractUser


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User(AbstractUser):
    STATE_CHOICES = [
        ("AC", "AC"),
        ("AL", "AL"),
        ("AP", "AP"),
        ("AM", "AM"),
        ("BA", "BA"),
        ("CE", "CE"),
        ("DF", "DF"),
        ("ES", "ES"),
        ("GO", "GO"),
        ("MA", "MA"),
        ("MT", "MT"),
        ("MS", "MS"),
        ("MG", "MG"),
        ("PA", "PA"),
        ("PB", "PB"),
        ("PR", "PR"),
        ("PE", "PE"),
        ("PI", "PI"),
        ("RJ", "RJ"),
        ("RN", "RN"),
        ("RS", "RS"),
        ("RO", "RO"),
        ("RR", "RR"),
        ("SC", "SC"),
        ("SP", "SP"),
        ("SE", "SE"),
        ("TO", "TO"),
    ]
    whatsapp = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    uf = models.CharField(choices=STATE_CHOICES, max_length=200, null=False)

    def __str__(self):
        return self.username


class Case(models.Model):
    ABERTO = "ABERTO"
    FINALIZADO = "FINALIZADO"

    STATUS = [
        (ABERTO, "Aberto"),
        (FINALIZADO, "Finalizado"),
    ]

    ong_name = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title_case = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=3000, null=True)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(choices=STATUS, default="ABERTO", null=False, max_length=11)
    datahora = models.DateTimeField(default=datetime.now, blank=False,)

    def __str__(self):
        return self.title_case
