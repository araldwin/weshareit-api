from rest_framework import generics, permissions
from weshareit_api.permissions import IsOwnerOrReadOnly
from loves.models import Love
from loves.serializers import LoveSerializer


class LoveList(generics.ListCreateAPIView):
    """
    List loves or create a love if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LoveSerializer
    queryset = Love.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LoveDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a love or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LoveSerializer
    queryset = Love.objects.all()