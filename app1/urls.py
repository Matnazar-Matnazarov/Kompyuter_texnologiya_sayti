from django.urls import path

from app1.views import AddTovar, Chiqarish, HomeDetail, update_quantity, VideoDetail, Video, \
    addvideo, Kompyuter_vs,Sanoq_sistema,Sonsanoqsistema,Sanoq,Home_asosiy

urlpatterns=[
    path('', Home_asosiy.as_view(), name="home"),
    path('lobaratoriya1/', Chiqarish.as_view(), name="lobaratoriya1"),

    path('home/<url>/', HomeDetail.as_view(), name="homedetail"),
    path('lobaratoriya2/<a>/', VideoDetail.as_view(), name="videodetail"),
    path('lobaratoriya2/', Video.as_view(), name="video"),
    path('addvideo/', addvideo.as_view(), name="addvideo"),
    path('addtovar/', AddTovar.as_view(), name="addtovar"),
    path('sanoq/sistema/',Sanoq_sistema.as_view(),name="sanoq_sistema"),
    path('sistema/sanoq/',Sonsanoqsistema.as_view(),name="son_sanoq"),
    path('sanoq/',Sanoq.as_view(),name="sanoq"),
    path('kompyuter/solishtirish/',Kompyuter_vs.as_view(),name="solishtirish"),
    path('update_quantity/<int:product_id>/<str:action>/', update_quantity.as_view(), name='update_quantity'),
]