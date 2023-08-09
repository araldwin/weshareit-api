from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from weshareit_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pin', 'parent_comment']

    def perform_create(self, serializer):
        parent_comment_id = self.request.data.get('parent_comment_id')  # Get the parent comment ID from the request data
        parent_comment = None
        if parent_comment_id:
            try:
                parent_comment = Comment.objects.get(id=parent_comment_id)
            except Comment.DoesNotExist:
                pass

        serializer.save(owner=self.request.user, parent_comment=parent_comment)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        parent_comment_id = request.data.get('parent_comment_id')
        parent_comment = Comment.objects.filter(pk=parent_comment_id).first()
        serializer = CommentSerializer(data=request.data)
        
        if parent_comment:
            if serializer.is_valid():
                serializer.validated_data['owner'] = self.request.user
                serializer.validated_data['pin'] = parent_comment.pin
                serializer.validated_data['parent_comment'] = parent_comment
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Parent comment does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
