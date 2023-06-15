from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('add/', views.add_student, name='add_student'),
]


