from django.urls import path, include
from project.user import views

urlpatterns = [
    path('users/', views.citizen_list)
]
