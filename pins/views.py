from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Pin
from .serializers import PinSerializer
from weshareit_api.permissions import IsOwnerOrReadOnly

class PinList(APIView):
    serializer_class = PinSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        pins = Pin.objects.all()
        serializer = PinSerializer(
            pins, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PinSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class PinDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PinSerializer

    def get_object(self, pk):
        try:
            pin = Pin.objects.get(pk=pk)
            self.check_object_permissions(self.request, pin)
            return pin
        except Pin.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pin = self.get_object(pk)
        serializer = PinSerializer(
            pin, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        pin = self.get_object(pk)
        serializer = PinSerializer(
            pin, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        pin = self.get_object(pk)
        pin.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
