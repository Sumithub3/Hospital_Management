
from django.contrib import admin
from django.urls import path, include
from patient_portal.views import HomepageView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/',include('staff_portal.urls'), name='stafff'),
    path('patient/',include('patient_portal.urls'), name='patientt'),
    path('', HomepageView.as_view(), name='home'),
]
