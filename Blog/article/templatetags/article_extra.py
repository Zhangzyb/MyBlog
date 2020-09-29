from django import template
from django.utils import timezone

from Blog.settings import TIME_ZERO, TIME_MIN, TIME_HOUR, TIME_MONTH, TIME_ONE, TIME_HALF_YEAR, DEFAULT_EMAIL
from comment.models import Comment
from ..models import Article, Tag, Category

register = template.Library()


@register.inclusion_tag('_recent_comment_post.html')
def get_recent():
    comment_list = Comment.objects.exclude(email=DEFAULT_EMAIL).order_by('-created_time')[:5]
    article_list = Article.objects.all().order_by('-views', '-create_time')[:5]
    return {
        'comment_list': comment_list,
        'article_list': article_list
    }


@register.inclusion_tag('_archive.html')
def archive():
    date_list = Article.objects.dates('create_time', 'month')
    return {
        'date_list': date_list
    }


@register.inclusion_tag('_tags.html')
def tag():
    tag_list = Tag.objects.all()
    return {
        'tag_list': tag_list
    }


@register.inclusion_tag('_category.html')
def category():
    category_list = Category.objects.filter(parent__isnull=True)
    return {
        'category_list': category_list
    }


@register.inclusion_tag('_subcategory.html', takes_context=True)
def subcategory(context):
    subcategory_list = Category.objects.filter(parent_id=context['category'].id)
    return {
        'subcategory_list': subcategory_list
    }


@register.filter(name='since_time')
def since_time(value):
    now = timezone.now()
    diff = now - value
    if diff.days == TIME_ZERO:
        if diff.seconds < TIME_MIN:
            return '刚刚'
        elif diff.seconds < TIME_HOUR:
            return str(diff.seconds // TIME_MIN) + '分钟前'
        else:
            return str(diff.seconds//TIME_HOUR) + '个小时前'
    elif TIME_ONE <= diff.days < TIME_MONTH:
        return str(diff.days) + '天前'
    elif diff.days < TIME_HALF_YEAR:
        return str(diff.days // TIME_MONTH) + '个月前'
    else:
        return value



