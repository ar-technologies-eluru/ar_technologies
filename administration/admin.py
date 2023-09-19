from django.contrib import admin
from django.contrib.auth.models import User,Group
from django.contrib.admin.models import LogEntry

from django.utils.html import format_html
from django.contrib.sessions.models import Session

from django.contrib.auth.models import User

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser','last_login','give_groups') # Added last_login
    def give_groups(self,obj):
        return str(obj.groups)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class AdminLogEntry(admin.ModelAdmin):
    list_display = ('action_time', 'user','content_type', 'object_repr','get_change_message')
    list_filter = ('action_flag','action_time')
    list_per_page = 25

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(LogEntry,AdminLogEntry)