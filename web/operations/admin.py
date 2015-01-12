from django.contrib import admin

# Register your models here.
from django.contrib import admin
from operations.models import *
from simple_history.admin import SimpleHistoryAdmin

for x in [Driver,Truck,Customer]:
	admin.site.register(x,SimpleHistoryAdmin)