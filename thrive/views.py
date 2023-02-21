from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Thrive
from .permissions import IsOwnerOrReadOnly
from .serializers import ThriveSerializer
from django.http import JsonResponse
import requests

def get_zen(request):
    # Make a GET request to the ZenQuotes API
    response = requests.get("https://zenquotes.io/api/today/")
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response to extract the quote
        data = response.json()[0]
        return JsonResponse(data)
    else:
        return print("Error: Unable to retrieve quote")
class ThriveList(ListCreateAPIView):
    queryset = Thrive.objects.all()
    serializer_class = ThriveSerializer


class ThriveDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Thrive.objects.all()
    serializer_class = ThriveSerializer
