
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('', views.index, name='index-list'),
    path('entryvalue/<str:name>', views.entryvalue, name='entry-value'),
]
