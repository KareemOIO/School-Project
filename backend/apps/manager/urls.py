# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('studentfilter/', views.StudentsFilterAPIView.as_view(), name='StudentsFilter'),
]
