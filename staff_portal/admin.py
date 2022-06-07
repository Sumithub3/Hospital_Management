from django.contrib import admin

from . models import Staff_Details, Staff_Leave_Details,Shift_Out_Timings, Shift_In_Timings

admin.site.register(Staff_Details)
admin.site.register(Shift_Out_Timings)
admin.site.register(Staff_Leave_Details)
admin.site.register(Shift_In_Timings)
