from django.urls import path
from . import views


urlpatterns = [
  path('get/',views.getApi, name='get'),
  path('post/',views.postApi, name='post'),
  path('update/<int:pk>',views.updateApi, name='updat'),
  path('delete/<int:pk>',views.deleteApi, name='delete'),
  path('all/',views.allApi, name='all'),
  path('all/<int:pk>',views.allApi, name='all'),
]