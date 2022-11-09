from rest_framework import serializers

from my.models import studentdata

class dataserializer(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()

    def create(self, validated_data):
        return studentdata.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.age=validated_data.get("age",instance.name)
        instance.save()
        return instance