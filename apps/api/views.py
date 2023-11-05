from django.db.models import Q
from .serializers import CategorySerializer, PostSerializer, PostSearchSerializer
from .models import Category, Post
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

class PostListView(ListAPIView):
    first_post = Post.objects.first()
    queryset = Post.objects.all().exclude(pk=first_post.pk)
    serializer_class = PostSerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['GET'])
def latest_post_api_view(request):
    if request.method == 'GET':
        latest_post = Post.objects.first()
        if latest_post:
            serializer = PostSerializer(latest_post)
            return Response(serializer.data)
        else:
            return Response({'message': 'No post found'}, status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def posts_list_view_from_category(request, slug):
    if request.method == 'GET':
        category_obj = Category.objects.get(slug=slug)
        posts = Post.objects.filter(categories=category_obj)
        posts_serializer = PostSerializer(posts, many=True)
        return Response(posts_serializer.data)

@api_view(['GET'])
def search_posts_api_view(request, name):
    if request.method == 'GET':
        posts = Post.objects.filter(Q(title__icontains=name) | Q(slug__icontains=name))
        if posts.exists():
            posts_serializer = PostSearchSerializer(posts, many=True)
            return Response(posts_serializer.data)
        else:
            return Response({'msg': 'No se encontró ningún artículo.'}, status=status.HTTP_204_NO_CONTENT)

