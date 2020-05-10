from rest_framework import serializers
from apps.core.models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id', 'text', 'access_token', 'is_viewed'
        )