from django.shortcuts import render, get_object_or_404
from .models import News,Category
def news_list(request):
    news = News.objects.all().order_by('-published_date')
    categories = Category.objects.all()
    return render(request, 'news_list.html', {
        'news_list': news,
        'categories': categories
    })
def news_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    news = News.objects.filter(category=category).order_by('-published_date')
    categories = Category.objects.all()
    return render(request, 'news_list.html', {
        'news_list': news,
        'categories': categories,
        'selected_category': category
    })
def latest_news(request):
    latest = News.objects.order_by('-published_date')
    return render(request, 'latest_news.html', {'latest_news': latest})
