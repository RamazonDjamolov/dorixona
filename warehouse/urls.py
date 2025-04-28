from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductWithUnitCreateView.as_view(), name='home'),
]