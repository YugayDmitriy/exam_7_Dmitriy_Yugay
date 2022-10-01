from django.contrib import admin
from .models import Visitors


class VisitorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'text', 'created_at', 'updated_at', 'status']
    list_filter = ['name', 'created_at', 'status']
    search_fields = ['name', 'created_at']
    fields = ['name', 'email', 'text', 'created_at', 'updated_at', 'status']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Visitors, VisitorsAdmin)
