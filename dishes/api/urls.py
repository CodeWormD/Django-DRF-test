from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FoodCategoryView

router = DefaultRouter()
router.register('foods', FoodCategoryView, basename='foods')

urlpatterns = [
    path('v1/', include(router.urls))
]