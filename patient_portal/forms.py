from django import forms
from .models import Patient_Details,City, Patient_Department_IPD, IPD_Patient_Beds

class Patient_Detail_Form(forms.ModelForm):
    class Meta:
        model = Patient_Details
        fields = '__all__'

class City_Form(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

class IPD_Department_Form(forms.ModelForm):
    class Meta:
        model = Patient_Department_IPD
        fields = '__all__'
class Bed_Create_Form(forms.ModelForm):
    class Meta:
        model = IPD_Patient_Beds
        fields = '__all__'
