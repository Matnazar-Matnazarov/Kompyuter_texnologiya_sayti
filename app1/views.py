from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import Tovarslar_s,Tur_lar_s, backet_s,Video_turi,Page2
from .forms import TovarslarForm, VideoForm

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
class Video(View):
    def get(self,request):
        turlari =Video_turi.objects.all()
        hammasi=Page2.objects.all()
        page=True
        return render(request,'video_home.html',{
                                            'turlar':turlari,
                                            'qidiruv': "ALL",
                                           'page':page,
                                            'hammasi':hammasi})
class VideoDetail(View):
    def get(self,request,a):
        page=False
        url=a
        turlari=Video_turi.objects.all()
        hammasi=Page2.objects.filter(turi__turi=a)
        return render(request,'video_home.html',{
                                            'turlar':turlari,
                                            'qidiruv': a,
                                           'page':page,
                                            'hammasi':hammasi})
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
            
class addvideo(LoginRequiredMixin,View):
    def get(self, request):
        if request.user.is_superuser:
            form = VideoForm()
            return render(request, 'addvideo.html', {'form': form})
        else:
            return redirect('video')
    def post(self, request):
        form = VideoForm(request.POST)
        if form.is_valid() and request.user.is_superuser:
            link = form.cleaned_data['you_tobe_linki']
            nomi = form.cleaned_data['nomi']
            turi = form.cleaned_data['turi']
            s = ""
            for i in link[::-1]:
                if i != '/':
                    s += i
                else:
                    break
            link = s[::-1]
            t = Video_turi.objects.get(turi=turi)
            video = Page2.objects.create(you_tobe_linki=link, nomi=nomi, turi=t)
            return redirect('video')
        else:
            return redirect('video')
class AddTovar(LoginRequiredMixin,View):
    def get(self,request):
        if request.user.is_superuser:
            form = TovarslarForm()
            return render(request, 'addtovar.html', {'form': form})
        else:
            return redirect('home')
    def post(self,request):
        if request.user.is_superuser:
            form = TovarslarForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        return redirect('home')
