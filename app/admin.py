from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import CustomerOrders
from datetime import datetime
from .forms import CustomerOrdersForm

class YourModelNameAdmin(admin.ModelAdmin):
    form = CustomerOrdersForm
    list_display = ('name', 'mobile', 'email')
    list_filter = ('name', 'created_by')
    search_fields = ('name', 'mobile', 'email')

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'mobile', 'email')
        }),
        ('Address Information', {
            'fields': ('address_line_1', 'address_line_2', 'near_by', 'village', 'mandal', 'district', 'state', 'country')
        }),
        ('Device Information', {
            'fields': ('device_type', 'assembled', 'brand', 'notes')
        }),
        ('Management Information', {
            'fields': ('service_engineer', 'operational_manager',)
        }),
    )
    def save_model(self, request, obj, form, change):
        user_obj = User.objects.get(id = request.user.id)
        if not change:
            obj.created_by = user_obj
        obj.updated_by = user_obj
        obj.save()

admin.site.register(CustomerOrders, YourModelNameAdmin)
