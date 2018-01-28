from django.urls import path, include
from rest_framework import routers
from project.preprocessor import views

urlpatterns = [
    # path('', include(router.urls)),
    path('save_data/', views.save_data)
]
