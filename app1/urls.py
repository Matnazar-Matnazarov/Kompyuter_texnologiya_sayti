from django.urls import path

from app1.views import AddTovar, Chiqarish, HomeDetail, update_quantity,VideoDetail,Video,addvideo
urlpatterns=[
    path('', Chiqarish.as_view(), name="home"),
    path('home/<url>/', HomeDetail.as_view(), name="homedetail"),
    path('lobaratoriya2/<a>/', VideoDetail.as_view(), name="videodetail"),
    path('lobaratoriya2/', Video.as_view(), name="video"),
    path('addvideo/', addvideo.as_view(), name="addvideo"),
    path('addtovar/', AddTovar.as_view(), name="addtovar"),
    path('update_quantity/<int:product_id>/<str:action>/', update_quantity.as_view(), name='update_quantity'),
]