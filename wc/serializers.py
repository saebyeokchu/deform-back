from rest_framework import serializers
from .models import blockboard

class blockboardSerializer(serializers.ModelSerializer) :
    userid = serializers.IntegerField()
    mediaid = serializers.IntegerField()
    shared = serializers.BooleanField()
    # createdat = serializers.DateTimeField()

    class Meta:
        model = blockboard
        fields = ['userid', 'mediaid', 'shared']


class authSerializer(serializers.ModelSerializer) :
    userid = serializers.IntegerField()
    token = serializers.CharField()
    verified = serializers.BooleanField()

    class Meta:
        model = blockboard
        fields = ['userid', 'token', 'verified']