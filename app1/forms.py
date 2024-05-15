# tovars/forms.py
from django import forms
from .models import Tovarslar_s, Video_turi

class TovarslarForm(forms.ModelForm):
    class Meta:
        model = Tovarslar_s
        fields = '__all__'  
class VideoForm(forms.Form):
    you_tobe_linki = forms.CharField(label='YouTube link', max_length=500)
    nomi = forms.CharField(label='Nomi', max_length=200)
    turi = forms.ModelChoiceField(queryset=Video_turi.objects.all(), empty_label=None)