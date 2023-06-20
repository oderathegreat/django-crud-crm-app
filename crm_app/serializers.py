from rest_framework import serializers
from .models import Trans


class TransSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trans
        fields = ('id', 'amount', 'transcode')

