from django.urls import path
from .views import (patient_information, IPD_Department_View, Check_Out_Patient_View,
    Beds_List_View, Patient_View,BedCreateView)

urlpatterns = [
    path('', patient_information.as_view(), name='patient'),
    path('ipd/', IPD_Department_View.as_view(), name='ipd'),
    path('beds/<pk>/delete/', Check_Out_Patient_View.as_view(), name='bed-del'),
    path('beds/', Beds_List_View.as_view(), name='bed-list'),
    path('beds/<pk>/', Check_Out_Patient_View.as_view(), name='bed-up'),
    path('list/', Patient_View.as_view(), name='patient-list'),
    path('bedcr/', BedCreateView.as_view(), name='bed-create'),

]