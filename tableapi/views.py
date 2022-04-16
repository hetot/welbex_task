from rest_framework import viewsets

from .serializers import SampleSerializer
from .models import Sample

# Create your views here.
class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
