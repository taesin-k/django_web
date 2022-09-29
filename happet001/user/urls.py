from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.index, name='index'),
    path('mall/',views.mall,name='mall'),
    path('board/',views.information,name='information'),
    path('search/',views.search,name='search'),
    path('board/<int:user_id>/',views.detail,name='detail'),
    path('mall/<int:product_id>/',views.product_detail,name='product_detail'),
    path('mall/pay/<int:product_id>/',views.pay,name='pay'),
]