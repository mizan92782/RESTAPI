from django.urls import path
from .views import StudentDetailAPIView

urlpatterns = [
    path('all/', StudentDetailAPIView.as_view(), name='func-api'),
    path('all/<int:pk>', StudentDetailAPIView.as_view(), name='func-api'),
]
