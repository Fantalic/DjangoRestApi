from rest_framework import serializers
from .models import PvYield

class PvYieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = PvYield
        fields = ('state', 'plz', 'yield_value')
        
    def create(self, validated_data):
        return PvYield.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.state = validated_data.get('state', instance.state)
        instance.plz = validated_data.get('plz', instance.plz)
        instance.yield_value = validated_data.get('yield_value', instance.yield_value)
        instance.save()
        return instance