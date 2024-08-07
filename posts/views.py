from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from .models import Post
from .has_user_id import HasUserId
from .post_owner import IsPostOwner
from .serializers import PostSerializer
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [HasUserId()]
        else:
            return [IsPostOwner()]

    def perform_create(self, serializer):
        try:
            user_id = self.request.data.get('user_id')
            if not user_id:
                raise ValidationError({"detail": "User ID must be provided."})
            serializer.save(user_id=user_id)
        except Exception as e:
            raise ValidationError({"detail": str(e)})

    def update(self, request, *args, **kwargs):
        try:
            post = self.get_object()
            user_id = request.data.get('user_id')
            if post.user_id != user_id:
                return Response({"detail": "You do not have permission to edit this post."}, status=status.HTTP_403_FORBIDDEN)
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            post = self.get_object()
            user_id = request.data.get('user_id')
            if post.user_id != user_id:
                return Response({"detail": "You do not have permission to delete this post."}, status=status.HTTP_403_FORBIDDEN)
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)