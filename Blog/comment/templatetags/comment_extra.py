from django import template
from ..forms import CommentForm

register = template.Library()


@register.inclusion_tag('_comment.html', takes_context=True)
def comment(context):
    form = CommentForm()
    article = context['article']
    comment_list = article.comment_set.all()
    comment_count = comment_list.count()
    return {
        'form': form,
        'article': article,
        'comment_list': comment_list,
        'comment_count': comment_count
    }