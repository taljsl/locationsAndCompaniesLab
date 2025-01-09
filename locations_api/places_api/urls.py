from django.urls import path
from . import views

urlpatterns = [
    path('api/places', views.PlaceList.as_view(), name = 'place_list'),
    path('api/places<int:pk>', views.PlaceDetail.as_view(), name = 'place_detail'),
]