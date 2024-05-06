from django.urls import path

from app1.views import Chiqarish, HomeDetail, Profile, update_quantity
urlpatterns=[
    path('', Chiqarish.as_view(), name="home"),
    path('home/<url>/', HomeDetail.as_view(), name="homedetail"),
    path('profile/', Profile.as_view(), name="profile"),
    path('update_quantity/<int:product_id>/<str:action>/', update_quantity.as_view(), name='update_quantity'),
]