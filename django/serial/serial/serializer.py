from rest_framework import serializers
from my.models import data

class dataSerializer(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()

    def create(self, validated_data):
        return data.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name=validate_data.get('name',instance.name)
        instance.age=validate_data.get('age',instance.age)
        instance.save()
        return instance
        