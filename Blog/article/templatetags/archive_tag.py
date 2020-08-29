from django import template
from article.models import Article, Tag

register = template.Library()


@register.inclusion_tag('archive.html')
def archive():
    date_list = Article.objects.dates('create_time', 'month')
    return {'date_list': date_list}


@register.inclusion_tag('tags.html')
def tag():
    tag_list = Tag.objects.all()
    return {'tag_list': tag_list}