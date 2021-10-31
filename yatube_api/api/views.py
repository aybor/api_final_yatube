from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Comment, Follow, Group, Post
from rest_framework import filters, permissions, viewsets
from rest_framework.exceptions import PermissionDenied

from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = None


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author_id != self.request.user.id:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author_id != self.request.user.id:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_destroy(instance)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = None
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post'])
        serializer.save(author=self.request.user, post=post)

    def list(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['post'])
        self.queryset = post.comments
        return super(CommentViewSet, self).list(request)

    def perform_update(self, serializer):
        if serializer.instance.author_id != self.request.user.id:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author_id != self.request.user.id:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_destroy(instance)


class FollowViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post')
    serializer_class = FollowSerializer
    pagination_class = None
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
