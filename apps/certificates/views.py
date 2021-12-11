from django.db.models import fields
from rest_framework import serializers, viewsets
from .models import Certificates


class CertificateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificateSerailizer
