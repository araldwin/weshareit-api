from rest_framework import generics, permissions
from weshareit_api.permissions import IsOwnerOrReadOnly
from .models import Pin
from .serializers import PinSerializer

class PinList(generics.ListCreateAPIView):
    """
    List pins or create a pin if logged in
    The perform_create method associates the pin with the logged in user.
    """
    serializer_class = PinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Pin.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PinDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a pin and edit or delete it if you own it.
    """
    serializer_class = PinSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Pin.objects.all()
