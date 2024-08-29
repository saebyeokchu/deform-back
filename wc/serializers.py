from rest_framework import serializers
from wc.models import Design

class DesignSerializer(serializers.ModelSerializer) :
    userId = serializers.IntegerField()
    list = serializers.CharField()

    class Meta:
        model = Design
        fields = ['list', 'userId']