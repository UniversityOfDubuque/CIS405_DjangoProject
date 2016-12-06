from django.contrib import admin

# Register your models here.
from .models import Student,Responds,Post,Products,Product_Type,Tours,Student_Tour,Tour_Destinations,Saudi_Group_Admins,Destination,Arrival,Student_Arrival

class ArrivalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Arrival, ArrivalAdmin)