from rest_framework.generics import ListAPIView, RetrieveAPIView
from eco.models import EcoPost
from .serializers import EcoSerializer


class EcoApiView(ListAPIView):
    queryset = EcoPost.objects.all()
    serializer_class = EcoSerializer

class DetailEco(RetrieveAPIView):
    queryset = EcoPost.objects.all()
    serializer_class = EcoSerializer

