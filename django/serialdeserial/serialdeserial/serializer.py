from rest_framework import serializers
from my.models import studentdata

class dataserializer(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()

    def create(self, validated_data):
        return studentdata.objects.create(**validated_data)

