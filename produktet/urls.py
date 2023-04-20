
from django.urls import path
from . import views

urlpatterns = [
    path('', views.produktet, name='produktet'),
   path('<int:id>/', views.produktet_detail, name='produktet_detail'),
]
