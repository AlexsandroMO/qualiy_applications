
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('', views.index, name='index-list'),
    path('task/<int:id>', views.taskview, name='task-view'),
    path('newtask/', views.newtask, name='new-task'),
    path('edit/<int:id>', views.editview, name='edit-view'),
    path('entryvalue/<str:name>', views.entryvalue, name='entry-value'),
]
