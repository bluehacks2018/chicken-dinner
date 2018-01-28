from django.urls import path, include
from rest_framework import routers
from project.dashboard import views

router = routers.DefaultRouter()
router.register('datasets', views.DatasetViewSet)
# router.register('tags', views.TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard_feed/', views.dashboard_feed),
    path('search/<tag>/', views.SearchDataset.as_view())
    # path('populate/<name>/', views.PopulateDataset.as_view())
]