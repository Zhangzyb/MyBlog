import markdown
from django.shortcuts import render, get_object_or_404
from article.models import Article, Tag


def index(request):
    post_list = Article.objects.all().order_by('-create_time')
    return render(request, 'index.html', context={'post_list': post_list})


def detail(request, english_name):
    article = get_object_or_404(Article, english_name=english_name)
    article.text = markdown.markdown(article.text,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                     ])
    return render(request, 'detail.html', context={'article': article})


def archive(request, year, month):
    article_list = Article.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
    date = {'year': year, 'month': month}
    return render(request, 'archive_article.html', context={'article_list': article_list, 'date': date})


def tag(request, name):
    article_list = Tag.objects.filter(name=name)
    return render(request, 'tag_article.html', context={'article_list':  article_list, 'name': name})