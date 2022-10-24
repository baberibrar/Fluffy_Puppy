from .views import BreedViewSet, DogViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'breeds', BreedViewSet, basename='breeds')
router.register(r'dogs', DogViewSet, basename='dogs')

urlpatterns = [
    path('', include(router.urls))
]
