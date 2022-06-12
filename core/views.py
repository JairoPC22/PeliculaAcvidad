from django.contrib.auth.models import User
# ViewSets define the view behavior.
from rest_framework import viewsets

from .models import Actor, Compania
from .serializers import ActorSerializers, CompaniSerializers


class ActorViewSet(viewsets.ModelViewSet):
    serializer_class = ActorSerializers
    queryset = Actor.objects.all()


class CompaniViewSet(viewsets.ModelViewSet):
    queryset = Compania.objects.all()
    serializer_class = CompaniSerializers
