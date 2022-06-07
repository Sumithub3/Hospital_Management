from django.contrib import admin
from . models import (Patient_Details, Patient_Medecines_details, IPD_Department_Details,IPD_Sub_Department_Details
, IPD_Patient_Beds, OPD_Department_Details,OPD_Sub_Department_Details,Patient_Department_IPD,State,
Diagnosis,City,Investigation_Test)

admin.site.register(Patient_Details)
admin.site.register(Patient_Medecines_details)
admin.site.register(IPD_Department_Details)
admin.site.register(IPD_Sub_Department_Details)
admin.site.register(IPD_Patient_Beds)
admin.site.register(OPD_Department_Details)
admin.site.register(OPD_Sub_Department_Details)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Patient_Department_IPD)
admin.site.register(Diagnosis)
admin.site.register(Investigation_Test)
