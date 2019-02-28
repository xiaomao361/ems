from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry

admin.site.register(models.Category)
admin.site.register(models.Brand)

admin.site.site_title="EMS manager"
admin.site.site_header="EMS manager"
admin.site.index_title="EMS manager"

@admin.register(models.Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('设备', {'fields': ['name', 'category', 'sn', 'brand', 'state', 'user', ]}),
        ('其他', {'fields': ['img', 'remark', 'procurement']}),
    ]
    list_display = ('name', 'state', 'user')
    list_filter = ['c_time']
    search_fields = ['sn', 'name', 'state']
    date_hierarchy = 'c_time'

@admin.register(models.User)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'department')
    search_fields = ['full_name', 'phone', 'email']

@admin.register(models.Merchant)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'phone', 'email', 'info')
    list_filter = ['type']

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    actions = None

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        return False