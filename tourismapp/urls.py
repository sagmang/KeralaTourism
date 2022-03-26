from django.urls import path
from .import views
urlpatterns = [
    path('',views.HOME,name='HOME'),
    path('SIGNIN',views.SIGNIN,name='SIGNIN'),
    path('SIGNUP',views.SIGNUP,name='SIGNUP'),
    path('MUNNAR',views.MUNNAR,name='MUNNAR'),
    path('ALAPPUZHA',views.ALAPPUZHA,name='ALAPPUZHA'),
    path('KANNUR',views.KANNUR,name='KANNUR'),
    path('KOZHIKODE',views.KOZHIKODE,name='KOZHIKODE'),
    path('CONTACT',views.CONTACT,name='CONTACT'),
]