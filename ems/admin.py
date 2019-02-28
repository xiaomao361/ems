from django.contrib import admin

from . import models

admin.site.register(models.User)
admin.site.register(models.Category)
admin.site.register(models.Equipment)
admin.site.register(models.Brand)
admin.site.register(models.Merchant)
