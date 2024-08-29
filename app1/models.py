from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class migrat(models.Model):
    nomi = models.IntegerField()


class Tur_lar_s(models.Model):
    mahsulot_turi = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.mahsulot_turi


class Tovarslar_s(models.Model):
    nomi = models.CharField(max_length=100)
    izohi = models.CharField(max_length=500)
    narxi = models.IntegerField()
    rasmi = models.ImageField()
    turi = models.ForeignKey(Tur_lar_s, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nomi


class backet_s(models.Model):
    mahsulot_id = models.ForeignKey(Tovarslar_s, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    soni = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.mahsulot_id.nomi


class Video_turi(models.Model):
    turi = models.CharField(max_length=200)

    def __str__(self):
        return self.turi


class Page2(models.Model):
    you_tobe_linki = models.CharField(max_length=500)
    nomi = models.CharField(max_length=200)
    turi = models.ForeignKey(Video_turi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomi


class Protsessor(models.Model):
    Protsessor_turi = [
        (3, "Core 3"),
        (5, "Core 5"),
        (7, "Core 7"),
        (9, "Core 9"),
    ]
    p_turi = models.IntegerField(choices=Protsessor_turi)

    def __str__(self) -> str:
        return f" Core {self.p_turi}"


class Operativka(models.Model):
    Operativ_xotira = [(1, "DDR"), (2, "DDR2"), (3, "DDR3"), (4, "DDR4"), (5, "DDR5")]
    o_turi = models.IntegerField(choices=Operativ_xotira)

    def __str__(self) -> str:
        return f"DDR{self.o_turi}"


class Ram_xotira(models.Model):
    ram = [
        (2, "2 GB RAM"),
        (4, "4 GB RAM"),
        (8, "8 GB RAM"),
        (12, "12 GB RAM"),
        (16, "16 GB RAM"),
        (24, "24 GB RAM"),
        (32, "32 GB RAM"),
        (64, "64 GB RAM"),
        (128, "128 GB RAM"),
    ]
    ram_x = models.IntegerField(choices=ram)

    def __str__(self):
        return f"{self.ram_x} GB RAM"


class Nomi_K(models.Model):
    nomi = models.CharField(max_length=200)

    def __str__(self):
        return self.nomi


class Yadro(models.Model):
    yadro = [
        (2, "2 yadro"),
        (4, "4 yadro"),
        (6, "6 yadro"),
        (8, "8 yadro"),
        (10, "10 yadro"),
        (12, "12 yadro"),
        (16, "16 yadro"),
        (18, "18 yadro"),
        (24, "24 yadro"),
        (32, "32 yadro"),
        (64, "64 yadro"),
    ]
    yadro_turi = models.IntegerField(choices=yadro)

    def __str__(self):
        return f"{self.yadro_turi} yadro"


class Sanoq_sistema_model(models.Model):
    sonlar = [
        (2, "2-lik sanoq tizimi (Binary)"),
        (3, "3-lik sanoq tizimi (Ternary)"),
        (4, "4-lik sanoq tizimi (Quaternary)"),
        (5, "5-lik sanoq tizimi (Quinary)"),
        (6, "6-lik sanoq tizimi (Senary)"),
        (8, "8-lik sanoq tizimi (Octal)"),
        (10, "10-lik sanoq tizimi (Decimal)"),
        (12, "12-lik sanoq tizimi (Duodecimal)"),
        (16, "16-lik sanoq tizimi (Hexadecimal)"),
    ]
    son = models.IntegerField(choices=sonlar)

    def __str__(self) -> str:
        return f"{self.son} sanoq sistema"
