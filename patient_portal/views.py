from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import Patient_Detail_Form, City_Form, IPD_Department_Form, Bed_Create_Form
from .models import Patient_Details, City, Patient_Department_IPD, IPD_Patient_Beds
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView


# Create your views here.


class HomepageView(TemplateView):
    template_name = 'index.html'

class patient_information(CreateView):
    model = Patient_Details
    form_class = Patient_Detail_Form

    def get_success_url(self):
        return reverse('patient')


class CityView(CreateView):
    model = City
    form_class = City_Form

    def get_success_url(self):
        return reverse('patient')


class IPD_Department_View(CreateView):
    model = Patient_Department_IPD
    form_class = IPD_Department_Form

    def get_success_url(self):
        return reverse('patient')


class Check_Out_Patient_View(DeleteView):
    model = IPD_Patient_Beds

    def get_success_url(self):
        return reverse('bed-list')


class BedCreateView(CreateView):
    model = IPD_Patient_Beds
    form_class = Bed_Create_Form

    def get_success_url(self):
        return reverse('bed-create')


class Beds_List_View(ListView):
    model = IPD_Patient_Beds

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['name']= Patient_Department_IPD.objects.all().filter('pid__name').values()
        return context

    def get_success_url(self):
        return reverse('patient')


class Patient_View(ListView):
    model = Patient_Details

    def get_success_url(self):
        return reverse('bed-del')
