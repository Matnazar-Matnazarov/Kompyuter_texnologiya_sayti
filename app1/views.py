from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import Tovarslar_s,Tur_lar_s, backet_s
class Chiqarish(View):
    def get(self,request):
        hammasi=Tovarslar_s.objects.all()
        product=backet_s.objects.filter(user_id=request.user.id)
        turlari=Tur_lar_s.objects.all()
        mas=[]
        for i in range(len(hammasi)):
                try:
                    h=True
                    for j in product:
                        if hammasi[i].id ==j.mahsulot_id.id and request.user.id==j.user_id.id:
                                if j.soni!=0:
                                    mas.append({"id" : hammasi[i].id,
                                    "mahsulot_nomi":  hammasi[i].nomi
                                        ,"mahsulot_izohi": hammasi[i].izohi,
                                        "rasm":hammasi[i].rasmi,
                                        "mahsulot_narxi":hammasi[i].narxi,
                                        "ulanma_id":j.mahsulot_id.id,
                                        "soni":j.soni
                                        })
                                    h=False
                                else:
                                    mas.append({"id": hammasi[i].id,
                                                "mahsulot_nomi": hammasi[i].nomi
                                                ,"mahsulot_izohi": hammasi[i].izohi,
                                                "rasm": hammasi[i].rasmi,
                                                "mahsulot_narxi": hammasi[i].narxi,
                                                "ulanma_id": j.mahsulot_id.id,
                                                "soni": j.soni
                                                })
                                    h=False
                    if h:
                        mas.append({"id": hammasi[i].id,
                                    "mahsulot_nomi": hammasi[i].nomi
                                    , "mahsulot_izohi": hammasi[i].izohi,
                                    "rasm": hammasi[i].rasmi,
                                    "mahsulot_narxi": hammasi[i].narxi,
                                    "ulanma_id": False,
                                    "soni": False
                                    })
                except:
                    mas.append({"id": hammasi[i].id,
                                "mahsulot_nomi": hammasi[i].nomi,
                                "mahsulot_izohi": hammasi[i].izohi,
                                "rasm": hammasi[i].rasmi,
                                "mahsulot_narxi": hammasi[i].narxi,
                                "ulanma_id":False,
                                "soni": False
                                })
        tanlanganlar=backet_s.objects.filter(user_id=request.user.id).order_by('id')
        summa=sum(i.mahsulot_id.narxi for i in tanlanganlar)
        return render(request,'home.html',{'mahsulotlar':mas,
                                            'turlar':turlari,
                                            'tanlangan':tanlanganlar,
                                            'qidiruv':"ALL",
                                            'summa':summa})
class HomeDetail(View):
    def get(self,request,url):
        hammasi=Tovarslar_s.objects.filter(turi__mahsulot_turi=url)
        product=backet_s.objects.filter(user_id=request.user.id)
        turlari=Tur_lar_s.objects.all()
        # turlari2=[i.mahsulot_turi for i in turlari if i.mahsulot_turi!=url]
        # print(turlari2)
        mas=[]
        for i in range(len(hammasi)):
                try:
                    h=True
                    for j in product:
                        if hammasi[i].id ==j.mahsulot_id.id and request.user.id==j.user_id.id:
                                if j.soni!=0:
                                    mas.append({"id" : hammasi[i].id,
                                    "mahsulot_nomi":  hammasi[i].nomi
                                        ,"mahsulot_izohi": hammasi[i].izohi,
                                        "rasm":hammasi[i].rasmi,
                                        "mahsulot_narxi":hammasi[i].narxi,
                                        "ulanma_id":j.mahsulot_id.id,
                                        "soni":j.soni
                                        })
                                    h=False
                                else:
                                    mas.append({"id": hammasi[i].id,
                                                "mahsulot_nomi": hammasi[i].nomi
                                                ,"mahsulot_izohi": hammasi[i].izohi,
                                                "rasm": hammasi[i].rasmi,
                                                "mahsulot_narxi": hammasi[i].narxi,
                                                "ulanma_id": j.mahsulot_id.id,
                                                "soni": j.soni
                                                })
                                    h=False
                    if h:
                        mas.append({"id": hammasi[i].id,
                                    "mahsulot_nomi": hammasi[i].nomi
                                    , "mahsulot_izohi": hammasi[i].izohi,
                                    "rasm": hammasi[i].rasmi,
                                    "mahsulot_narxi": hammasi[i].narxi,
                                    "ulanma_id": False,
                                    "soni": False
                                    })
                except:
                    mas.append({"id": hammasi[i].id,
                                "mahsulot_nomi": hammasi[i].nomi,
                                "mahsulot_izohi": hammasi[i].izohi,
                                "rasm": hammasi[i].rasmi,
                                "mahsulot_narxi": hammasi[i].narxi,
                                "ulanma_id":False,
                                "soni": False
                                })
        tanlanganlar=backet_s.objects.filter(user_id=request.user.id).order_by('id')
        summa=sum(i.mahsulot_id.narxi for i in tanlanganlar)
        return render(request,'home.html',{'mahsulotlar':mas,
                                            'turlar':turlari,
                                            'tanlangan':tanlanganlar,
                                            'qidiruv':url,
                                            'summa':summa})
class update_quantity(LoginRequiredMixin,View):
        def get(self,request, product_id, action):
            if request.user.is_authenticated:
                mahsulot=Tovarslar_s.objects.get(id=product_id)
                tovar=backet_s.objects.filter(mahsulot_id=product_id,user_id=request.user.id)
                if tovar:
                    r=False
                    if action == 'increase':
                        tovar[0].soni += 1
                        tovar[0].save()
                        r=True
                    elif action == 'decrease':
                        backet_s.objects.filter(mahsulot_id=product_id,user_id=request.user.id).delete()
                    if r:
                        mal=backet_s.objects.filter(user_id=request.user.id,soni__gt=0)
                        return JsonResponse({'new_quantity': tovar[0].soni})
                    else:
                         return JsonResponse({'new_quantity': False})
                else:
                    backet_s.objects.create( 
                        mahsulot_id = mahsulot,
                        user_id = request.user
                    )
                    tovar=backet_s.objects.filter(mahsulot_id=product_id,user_id=request.user.id)
                    mah_narxi=tovar[0].mahsulot_id.narxi*tovar[0].soni
                    mal=backet_s.objects.filter(user_id=request.user.id,soni__gt=0)
                    jami_summa=sum(i.soni*i.mahsulot_id.narxi for i in mal)
                    return JsonResponse({'new_quantity': tovar[0].soni,
                                        'mah_narxi' : mah_narxi,
                                        'summa':jami_summa})
            else:
                return JsonResponse({'error': 'User is not authenticated'}, status=401)
class Profile(LoginRequiredMixin,View):
     def get(self,request):
          malumot=backet_s.objects.filter(user_id=request.user.id,soni__gt=0)
          jami_summa=sum(i.soni*i.mahsulot_id.narxi for i in malumot)
          mal=[]
          for i in malumot:
               mal.append({
                    'id':i.id,
                    'mahsulot_id' :i.mahsulot_id,
                    'soni':i.soni,
                    'user_id':i.user_id,
                    'mahsulot_narxi':i.soni*i.mahsulot_id.narxi
               })
          return render(request,'profile.html',{'mahsulotlar':mal,
                                            'summa':jami_summa})