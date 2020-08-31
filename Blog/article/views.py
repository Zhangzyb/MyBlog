import markdown
from django.shortcuts import render, get_object_or_404
from article.models import Article, Tag, Category


def index(request):
    article_list = Article.objects.all()
    return render(request, 'index.html', context={'article_list': article_list})


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
    info = {
        'info': f'{year}/{month}'
    }
    return render(request, 'index.html', context={'article_list': article_list, 'info': info})


def tag(request, name):
    tag_id = Tag.objects.filter(name=name).first()
    article_list = Article.objects.filter(tag=tag_id)
    info = {
        'info': name
    }
    return render(request, 'index.html', context={'article_list':  article_list, 'info': info})


def category(request, cate_name):
    category_id = Category.objects.filter(cate_name=cate_name).first()
    article_list = Article.objects.filter(category=category_id)
    info = {
        'info': cate_name
    }
    return render(request, 'index.html', context={'article_list': article_list, 'info': info})