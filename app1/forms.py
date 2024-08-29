from django import forms
from .models import (
    Tovarslar_s,
    Video_turi,
    Ram_xotira,
    Protsessor,
    Operativka,
    Nomi_K,
    Yadro,
    Sanoq_sistema_model,
)
from django.core.validators import MinValueValidator, MaxValueValidator


class TovarslarForm(forms.ModelForm):
    class Meta:
        model = Tovarslar_s
        fields = "__all__"


class VideoForm(forms.Form):
    you_tobe_linki = forms.CharField(label="YouTube link", max_length=500)
    nomi = forms.CharField(label="Nomi", max_length=200)
    turi = forms.ModelChoiceField(queryset=Video_turi.objects.all(), empty_label=None)


class Kompyuter_solishtirish(forms.Form):
    komp_model_1 = forms.ModelChoiceField(
        queryset=Nomi_K.objects.all(), empty_label=None, label="Model 1"
    )
    komp_protsessor_1 = forms.ModelChoiceField(
        queryset=Protsessor.objects.all(), empty_label=None, label="Processor 1"
    )
    komp_ram_1 = forms.ModelChoiceField(
        queryset=Ram_xotira.objects.all(), empty_label=None, label="RAM 1"
    )
    komp_operativka_1 = forms.ModelChoiceField(
        queryset=Operativka.objects.all(),
        empty_label=None,
        label="Operational Memory 1",
    )
    komp_yadro_1 = forms.ModelChoiceField(
        queryset=Yadro.objects.all(), empty_label=None, label="Core 1"
    )

    komp_model_2 = forms.ModelChoiceField(
        queryset=Nomi_K.objects.all(), empty_label=None, label="Model 2"
    )
    komp_protsessor_2 = forms.ModelChoiceField(
        queryset=Protsessor.objects.all(), empty_label=None, label="Processor 2"
    )
    komp_ram_2 = forms.ModelChoiceField(
        queryset=Ram_xotira.objects.all(), empty_label=None, label="RAM 2"
    )
    komp_operativka_2 = forms.ModelChoiceField(
        queryset=Operativka.objects.all(),
        empty_label=None,
        label="Operational Memory 2",
    )
    komp_yadro_2 = forms.ModelChoiceField(
        queryset=Yadro.objects.all(), empty_label=None, label="Core 2"
    )


class Sanoq_form(forms.Form):
    kiritilgan_son = forms.IntegerField(
        label="10 lik sanoq sistemadagi sonni kiriting ",
        validators=[MinValueValidator(0), MaxValueValidator(10000000000000000000)],
    )
    son = forms.ModelChoiceField(
        queryset=Sanoq_sistema_model.objects.all(),
        empty_label=None,
        label="O'tkazmoqchi bo'lgan sanoq sistemani kiriting ",
    )


class Sonsanoq(forms.Form):
    kiritilgan_son = forms.CharField(label="Qiymatni kiriting :", max_length=500)
    son = forms.ModelChoiceField(
        queryset=Sanoq_sistema_model.objects.all(),
        empty_label=None,
        label="Kiritmoqchi bo'lgan Sanoq sistemani tanlang :",
    )
