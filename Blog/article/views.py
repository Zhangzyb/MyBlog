import markdown
from django.shortcuts import render, get_object_or_404
from .models import Article, Tag, Category


def index(request):
    article_list = Article.objects.all()
    return render(request, 'index.html', context={'article_list': article_list})


def detail(request, english_name):
    article = get_object_or_404(Article, english_name=english_name)
    if request.user != article.author:
        article.inc_views()
    pre_article = Article.objects.filter(id__lt=article.id).order_by('-id').first()
    next_article = Article.objects.filter(id__gt=article.id).order_by('id').first()
    comment_count = article.comment_set.all().count()
    article.text = markdown.markdown(article.text,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                     ])
    return render(request, 'detail.html', context={
        'article': article,
        'comment_count': comment_count,
        'pre_article': pre_article,
        'next_article': next_article
    })


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