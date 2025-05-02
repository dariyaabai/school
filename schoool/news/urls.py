from django.urls import path
from . import views
from .views import news_list, news_by_category, latest_news

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('category/<str:category_name>/', news_by_category, name='news_by_category'),
    path('latest/', views.latest_news, name='latest_news'),
    path('news/',views.news_list,name='news-list'),
]