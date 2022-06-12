from rest_framework import serializers
from .models import Actor, Compania


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Actor


class CompaniSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Compania
