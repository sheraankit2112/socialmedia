from rest_framework import serializers

from my.models import mydata

class dataserializer(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()

    def create(self, validated_data):
        return mydata.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.age=validated_data.get("age",instance.age)
        instance.save()
        return instance