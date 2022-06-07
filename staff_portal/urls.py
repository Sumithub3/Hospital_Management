from django.contrib import admin
from django.urls import path
from .views import (Staff_information, Staff_List, StaffUpdateView,
                    Staff_In_View,Staff_Out_View,Shift_List,Shift_detail_List)

urlpatterns = [
    path('', Staff_information.as_view(), name='staff_login'),
    path('list/', Staff_List.as_view(), name='staff_list'),
    path('update/<pk>', StaffUpdateView.as_view(), name='staff_update'),
    path('in/', Staff_In_View.as_view(), name='in'),
    path('out/', Staff_Out_View.as_view(), name='out'),
    path('shift/', Shift_List.as_view(), name='shift'),
    path('time/', Shift_detail_List.as_view(), name='time'),
]
