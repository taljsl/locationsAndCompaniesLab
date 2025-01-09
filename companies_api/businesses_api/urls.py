from django.urls import path
from . import views

urlpatterns = [
    path('api/businesses', views.BusinessList.as_view(), name = 'business_list'),
    path('api/businesses<int:pk>', views.BusinessDetail.as_view(), name = 'business_detail')
]