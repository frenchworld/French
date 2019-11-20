
from django.contrib import admin
from django.urls import path

from FrenchVo import views

urlpatterns = [
    path('', views.home),
    path('home/', views.index),
    path('phrase', views.phrase),
    path('erending', views.erending),
    path('reending', views.reending),
    path('irending', views.irending),

]
