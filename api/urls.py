from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailEco.as_view()),
    path('', EcoApiView.as_view()),
]