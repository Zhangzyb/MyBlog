import markdown
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article, Tag, Category


def index(request):
    articles = Article.objects.all().order_by('-create_time')
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    article_list = paginator.get_page(page_number)
    page_range = pagination(article_list)
    return render(request, 'index.html', context={'article_list': article_list, 'page_range': page_range})


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
    articles = Article.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    article_list = paginator.get_page(page_number)
    page_range = pagination(article_list)
    info = {'info': f'{year}/{month}'}
    return render(request, 'index.html', context={'article_list': article_list, 'info': info, 'page_range': page_range})


def tag(request, name):
    tag_id = Tag.objects.filter(name=name).first()
    articles = Article.objects.filter(tag=tag_id).order_by('-create_time')
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    article_list = paginator.get_page(page_number)
    page_range = pagination(article_list)
    info = {'info': name}
    return render(request, 'index.html', context={'article_list':  article_list, 'info': info, 'page_range': page_range})


def category(request, cate_name):
    category_id = Category.objects.filter(cate_name=cate_name).first()
    articles = Article.objects.filter(category=category_id).order_by('-create_time')
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    article_list = paginator.get_page(page_number)
    page_range = pagination(article_list)
    info = {'info': cate_name}
    return render(request, 'index.html', context={'article_list': article_list, 'info': info, 'page_range': page_range})


def pagination(article_list):
    page = article_list.number
    page_range = list(range(max(page - 2, 1), min(page + 3, article_list.paginator.num_pages + 1)))
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if article_list.paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != article_list.paginator.num_pages:
        page_range.append(article_list.paginator.num_pages)
    return page_range