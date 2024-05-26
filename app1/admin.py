from django.contrib import admin

# Register your models here.
from .models import  Tovarslar_s,Tur_lar_s, backet_s,Video_turi,Page2,Ram_xotira,Protsessor,Operativka,Nomi_K,Yadro,Sanoq_sistema_model

class Tur_lar_s_Admin(admin.ModelAdmin):
    search_fields=['mahsulot_turi']
    list_display=['mahsulot_turi']
class Tovarslar_Admin(admin.ModelAdmin):
    search_fields=['nomi','izohi','narxi','rasmi']
    list_display=['nomi','izohi','narxi','rasmi','turi']
class backet_s_Admin(admin.ModelAdmin):
    search_fields=['soni']
    list_display=['mahsulot_id','user_id','soni']
class Page_Admin(admin.ModelAdmin):
    search_fields=['nomi','you_tobe_linki']
    list_display=['nomi','you_tobe_linki','turi']

class Video_turiAdmin(admin.ModelAdmin):
    search_fields=['turi']
    list_display=['turi']
class Ram_Admin(admin.ModelAdmin):
    search_fields=['ram_x']
    list_display=['ram_x']
class Protsessor_turi_Admin(admin.ModelAdmin):
    search_fields=['p_turi']
    list_display=['p_turi']
class Operativ_xotira_Admin(admin.ModelAdmin):
    search_fields=['o_turi']
    list_display=['o_turi']
class Nomi_k_admin(admin.ModelAdmin):
    search_fields=['nomi']
    list_display=['nomi']
class Yadro_Admin(admin.ModelAdmin):
    search_fields=['yadro_turi']
    list_display=['yadro_turi']
class Sanoq_admin(admin.ModelAdmin):
    search_fields=['son']
    list_display=['son']
admin.site.register(Tovarslar_s,Tovarslar_Admin)
admin.site.register(Tur_lar_s,Tur_lar_s_Admin)
admin.site.register(backet_s,backet_s_Admin)
admin.site.register(Video_turi,Video_turiAdmin)
admin.site.register(Page2,Page_Admin)
admin.site.register(Ram_xotira,Ram_Admin)
admin.site.register(Protsessor,Protsessor_turi_Admin)
admin.site.register(Operativka,Operativ_xotira_Admin)
admin.site.register(Nomi_K,Nomi_k_admin)
admin.site.register(Yadro,Yadro_Admin)
admin.site.register(Sanoq_sistema_model,Sanoq_admin)