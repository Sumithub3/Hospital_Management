from django import forms
from .models import Staff_Details, Staff_Leave_Details, Shift_Out_Timings, Shift_In_Timings


class PartialAuthorForm(forms.ModelForm):
    class Meta:
        model = Staff_Details
        fields = '__all__'

class leaves_Management_Form(forms.ModelForm):
    class Meta:
        model = Staff_Leave_Details
        fields = '__all__'

class Staff_In_Form(forms.ModelForm):
    class Meta:
        model = Shift_In_Timings
        fields = '__all__'


class Staff_Out_Form(forms.ModelForm):
    class Meta:
        model = Shift_Out_Timings
        fields ='__all__'