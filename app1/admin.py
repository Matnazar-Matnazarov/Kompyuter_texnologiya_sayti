from django.contrib import admin

# Register your models here.
from .models import  Tovarslar_s,Tur_lar_s, backet_s,Video_turi,Page2
admin.site.register(Tovarslar_s)
admin.site.register(Tur_lar_s)
admin.site.register(backet_s)
admin.site.register(Video_turi)
admin.site.register(Page2)