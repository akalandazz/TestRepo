from django.urls import path, include
from . import views

from rest_framework import routers
app_name = 'persons'
router = routers.DefaultRouter()
router.register('shifts', views.ShiftsViewSet)
router.register('morning_shifts', views.MorningShiftViewSet)
router.register('midday_shifts', views.MiddayShiftViewSet)
router.register('night_shifts', views.NightShiftViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('shift/<pk>/enroll/<slug:name>', views.ShiftEnrollView.as_view(), name='shift_enroll'),
]