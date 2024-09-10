from django.urls import path
from . import views 

urlpatterns = [
    path('cadastra/', views.cadastrar)
]