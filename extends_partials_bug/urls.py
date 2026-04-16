from django.urls import path

from . import views

urlpatterns = [
    path('', views.Base.as_view()),
    path('extended', views.Extended.as_view()),
]
