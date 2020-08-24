import markdown
from django.shortcuts import render, get_object_or_404
from article.models import Article


def index(request):
    post_list = Article.objects.all().order_by('-create_time')
    return render(request, 'index.html', context={'post_list': post_list})


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.text = markdown.markdown(article.text,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                     ])
    return render(request, 'detail.html', context={'article':article})