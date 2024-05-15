from django.urls import path
from . import views


urlpatterns = [
    path('', views.cgpa_calculator, name='cgpa_calculator'),
    path('edit/<int:subject_id>/', views.edit_subject, name='edit_subject'),
    path('delete/<int:subject_id>/', views.delete_subject, name='delete_subject'),
    path('result/', views.result, name='result'),
]
  