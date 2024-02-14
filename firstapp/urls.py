from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('/<int:pk>', views.detail_student, name='detail_student'),
    path('add/', views.add_student, name='add_student'),
]


