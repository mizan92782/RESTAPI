from django.urls import path
from . import views

urlpatterns = [
    
    path('allapi/<int:pk>/',views.StudentMixin.as_view(), name='mixin'),
    path('allapi/',views.StudentMixin.as_view(), name='mixinPk'),
]
