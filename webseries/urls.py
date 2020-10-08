from django.urls import path
from . import views

urlpatterns = [
    path('', views.series, name="series"),
    path('hindimovies/', views.hindimovies, name="hindimovies"),
    path('contentextendseries/', views.contentextendseries, name="contentextendseries"),
    path('contentextendserieshindi/', views.contentextendserieshindi, name="contentextendserieshindi"),
    path('contentextendmovies/', views.contentextendmovies, name="contentextendmovies"),
    path('contentextendmovieshindi/', views.contentextendmovieshindi, name="contentextendmovieshindi"),
    path('movies/', views.movies, name="movies"),
    path('hindiseries/', views.hindiseries, name="hindiseries"),
    path('search/', views.search, name="search"),
    # path('trending_search/', views.trendingSearch, name="trending_search"),
    path('FileNotFound/', views.FileNotFound, name="FileNotFound"),
    path('download/<int:sid>', views.download, name="download"),
    path('trending/<int:sid>', views.trending, name="trending"),
]