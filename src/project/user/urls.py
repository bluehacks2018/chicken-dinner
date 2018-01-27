from django.urls import path, include
from rest_framework import routers
from project.user import views

router = routers.DefaultRouter()
router.register('citizens', views.CitizenViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all', views.citizen_list)
]
