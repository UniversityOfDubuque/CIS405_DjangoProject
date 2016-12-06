from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Student,Responds,Post,Products,Product_Type,Tours,Student_Tour,Tour_Destinations,Saudi_Group_Admins,Destination,Arrival,Student_Arrival

class IndexView(generic.ListView):
    template_name = 'SaudiStudentOrganization/index.html'
    context_object_name = 'latest_arrival_list'

    def get_queryset(self):
        """Return the last five arrivals."""
        return Arrival.objects.order_by('-Arrival_Date_Time')[:5]