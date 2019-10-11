from django.urls import path

from .views import *

app_name = 'reservation'

urlpatterns = [
    path('create/', ReservationCreate.as_view(), name='create'),
    path('update/<int:pk>/', ReservationUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ReservationDelete.as_view(), name='delete'),
    path('detail/<int:pk>/', ReservationDetail.as_view(), name='detail'),
    path('', ReservationList.as_view(), name='list'),
]