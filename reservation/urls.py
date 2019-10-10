from django.urls import path

from .views import *

app_name = 'reservation'

urlpatterns = [
    path('create/', reservation_create, name='create'),
    path('update/<int:reservation_id>/', reservation_update, name='update'),
    path('delete/<int:pk>/', ReservationDelete.as_view(), name='delete'),
    path('detail/<int:pk>/', ReservationDetail.as_view(), name='detail'),
    path('', ReservationList.as_view(), name='list'),
]