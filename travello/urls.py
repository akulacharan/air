from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('place',views.place,name='place'),
    path('news',views.news,name='news'),
    path('home',views.home,name='home'),
    path('con',views.con,name='con')
    ]