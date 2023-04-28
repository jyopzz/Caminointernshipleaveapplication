from django.contrib import admin

from leaveapp.views import leavedetails
from.models import Leaveapply,Leavedetails,Admindata



# Register your models here.
admin.site.register(Leaveapply)
admin.site.register(Leavedetails)


admin.site.register(Admindata)
