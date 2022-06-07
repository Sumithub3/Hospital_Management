from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Staff_Details, Staff_Leave_Details, Shift_Out_Timings, Shift_In_Timings
from .forms import PartialAuthorForm,leaves_Management_Form,Staff_In_Form, Staff_Out_Form
from django.urls import reverse
from django.views.generic.list import ListView
from django.urls import reverse
from datetime import datetime


class Staff_information(CreateView):
    model = Staff_Details
    form_class = PartialAuthorForm

    def get_success_url(self):
        return reverse('staff_login')

class Staff_List(ListView):
    model = Staff_Details

    def get_queryset(self, *args, **kwargs):
        qs = super(Staff_List, self).get_queryset(*args, **kwargs)
        return qs

    def get_context_data(self, **kwargs):
        context = super(Staff_List, self).get_context_data(**kwargs)
        context['leaves'] =Staff_Details.objects.all()
        return context

    def get_success_url(self):
        return reverse('staff_list')


class StaffUpdateView(UpdateView):
    model = Staff_Details
    form_class = leaves_Management_Form

    def get_success_url(self):
        return reverse('staff_list')

class Staff_In_View(CreateView):
    model = Shift_In_Timings
    form_class = Staff_In_Form

    def get_success_url(self):
        return reverse('staff_list')

class Staff_Out_View(CreateView):
    model = Shift_Out_Timings
    form_class = Staff_Out_Form

    def get_success_url(self):
        return reverse('staff_list')


class Shift_List(ListView):
    model = Staff_Details
    def get_queryset(self, *args, **kwargs):
        qs = super(Shift_List, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("created_date")
        return qs

    def get_context_data(self, **kwargs):
        context = super(Shift_List, self).get_context_data(**kwargs)
        context['staff_list'] = Staff_Details.objects.all()
        # Add any other variables to the context here
        return context

class Shift_detail_List(ListView):


    def get_queryset(self):
        qs = Staff_Leave_Details.objects.all()
        Shift_Timings.objects.create(name_id=2,entry='07:40:00',out='06:30:00',leaves = True)

        return qs

