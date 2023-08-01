from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brand/<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('team/', views.team, name='team'),
]
