from rest_framework import serializers
from .models import Sample


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sample
        fields = ("date", "name", "quantity", "distance")
