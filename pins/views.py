from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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
    queryset = Pin.objects.annotate(
        loves_count=Count('loves', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'loves_count',
        'comments_count',
        'loves__created_at',
    ]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PinDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a pin and edit or delete it if you own it.
    """
    serializer_class = PinSerializer
    queryset = Pin.objects.annotate(
        loves_count=Count('loves', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
