from django.shortcuts import render, redirect
from .models import Article
from .form import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' :articles
    }
    return render(request, 'articles/index.html', context)


def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' :form
    }
    return render(request, 'articles/new.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    
    if form.is_valid():
        form.save()
        return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' :form
    }
    return render(request, 'articles/new.html', context)