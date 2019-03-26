from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(models.Category)
admin.site.register(models.Brand)
admin.site.register(models.Notice)
admin.site.register(models.OpenApp)
admin.site.register(models.Joke)
# admin.site.register(models.Risk)
admin.site.register(models.Chat)
# admin.site.register(models.Could_sell)

admin.site.site_title = "EMS manager"
admin.site.site_header = "EMS manager"
admin.site.index_title = "EMS manager"

# @admin.register(models.Equipment)


class EquipmentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('设备', {'fields': ['name', 'category',
                           'sn', 'brand', 'state', 'user', ]}),
        ('其他', {'fields': ['img', 'remark', 'procurement',
                           'price_in', 'maintain', 'price_out']}),
    ]
    list_display = ('name', 'state', 'user')
    list_filter = ['c_time']
    search_fields = ['sn', 'name', 'state']
    date_hierarchy = 'c_time'


class EquipmentHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['name', 'sn', 'state', 'remark']


admin.site.register(models.Equipment, EquipmentHistoryAdmin)


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'department')
    search_fields = ['full_name', 'phone', 'email']


@admin.register(models.Merchant)
class MerchantAdmin(admin.ModelAdmin):
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

@admin.register(models.Risk)
class RiskAdmin(admin.ModelAdmin):
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

@admin.register(models.Could_sell)
class Could_sellAdmin(admin.ModelAdmin):
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