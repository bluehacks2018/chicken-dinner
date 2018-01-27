from django.urls import path, include
from rest_framework import routers
from project.dashboard import views

router = routers.DefaultRouter()
router.register('datasets', views.DatasetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dataset_feed', views.dashboard_feed)
]
