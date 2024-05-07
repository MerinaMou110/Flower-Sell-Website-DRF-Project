from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers

class ContactusViewset(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactUsSerializer