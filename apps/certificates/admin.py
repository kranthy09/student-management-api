from django.contrib import admin
from .models import Certificates


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    search_fields = ('name', )


admin.site.register(Certificates, CertificateAdmin)
