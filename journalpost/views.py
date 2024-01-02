from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from .serializers import ArticleSerializer
from .models import Article

class ArticleListView(APIView):
    @parser_classes([JSONParser])
    def get(self, request):
        if request.GET:
            articles = Article.objects.filter(category=request.GET.get('category')).order_by('-id')[:50]
        else:
            articles = Article.objects.all().order_by('-id')[:50]
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

class ArticleDetailView(APIView):
    @parser_classes([JSONParser])
    def get(self, request):
        if request.GET:
            article = Article.objects.get(pk=request.GET.get('id'))
            serializer = ArticleSerializer(article, many=False)
            return JsonResponse(serializer.data, safe=False)

class ArticleSearchView(APIView):
    @parser_classes([JSONParser])
    def get(self, request):
        if request.GET:
            articles = Article.objects.filter(title__icontains=request.GET.get('query'))

            # Use DRF's PageNumberPagination
            paginator = PageNumberPagination()
            paginator.page_size = 10

            paginated_articles = paginator.paginate_queryset(articles, request)

            serializer = ArticleSerializer(paginated_articles, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            # Handle other HTTP methods if needed
            return JsonResponse({"error": "Invalid request method"}, status=405)
