from django.contrib import admin
from django.urls import path
from core.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view()),
]
