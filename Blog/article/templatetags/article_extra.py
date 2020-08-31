from django import template
from article.models import Article, Tag, Category

register = template.Library()


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