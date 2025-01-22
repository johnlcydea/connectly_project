from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer


# Home view
def home(request):
    return HttpResponse("Welcome to the Connectly Project Home Page!")


# Index view to list all posts
@api_view(['GET'])
def index(request):
    posts = Post.objects.all()
    posts_data = [{'id': post.id, 'title': post.title, 'content': post.content} for post in posts]
    return Response({'posts': posts_data})


# Detail view to show a single post
@api_view(['GET'])
def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_data = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author_id': post.author_id,
    }
    return Response({'post': post_data})


# Create a new post
@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)  # Pass request data to the serializer
    if serializer.is_valid():  # Check if data is valid
        serializer.save()  # Save the validated data to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
