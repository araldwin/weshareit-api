from django.db import IntegrityError
from rest_framework import serializers
from loves.models import Love

class LoveSerializer(serializers.ModelSerializer):
    """
    Serializer for the Love model
    The create method handles the unique constraint on 'owner' and 'pin'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Love
        fields = ['id', 'created_at', 'owner', 'pin']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })