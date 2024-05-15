from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class migrat(models.Model):
    nomi=models.IntegerField()

class Tur_lar_s(models.Model):
    mahsulot_turi=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.mahsulot_turi
class Tovarslar_s(models.Model):
    nomi=models.CharField(max_length=100)
    izohi=models.CharField(max_length=500)
    narxi=models.IntegerField()
    rasmi=models.ImageField()
    turi=models.ForeignKey(Tur_lar_s,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nomi
class backet_s(models.Model):
    mahsulot_id=models.ForeignKey(Tovarslar_s,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    soni=models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.mahsulot_id.nomi
class Video_turi(models.Model):
    turi=models.CharField(max_length=200)
    def __str__(self):
        return self.turi
class Page2(models.Model):
    you_tobe_linki=models.CharField(max_length=500)
    nomi=models.CharField(max_length=200)
    turi=models.ForeignKey(Video_turi,on_delete=models.CASCADE)
    def __str__(self):
        return self.nomi