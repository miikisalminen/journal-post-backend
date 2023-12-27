from django.contrib import admin
from django.urls import path, re_path, include
from django.http import HttpResponse
from django.shortcuts import render
from .views import ArticleListView, ArticleDetailView, ArticleSearchView

app_name = "journalpost"

urlpatterns = [
    # API-Endpoints
    path('api/articles/', ArticleListView.as_view()),
    path('api/article_by_id/', ArticleDetailView.as_view()),
    path('api/search/', ArticleSearchView.as_view())
]
