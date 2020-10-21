from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from .forms import CommentForm
from article.models import Article
from .models import Comment
from celery_tasks.email.tasks import send_comment_email, send_sub_comment_email

@require_POST
def comment(request, english_name):
    article = Article.objects.get(english_name=english_name)
    form = CommentForm(request.POST)
    QQ = request.POST.get('email')
    QQ = QQ[:QQ.find('@')]
    img_url = f'https://q.qlogo.cn/headimg_dl?dst_uin={QQ}&spec=100'
    comment_ins = form.save(commit=False)
    comment_ins.article = article
    comment_ins.img_url = img_url
    comment_ins.save()
    detail_url = request.META.get('HTTP_REFERER') + '#comment-area'
    send_comment_email.delay(comment_ins.name, article.title, detail_url)
    return redirect(reverse('article:detail', kwargs={'english_name': english_name}))


@require_POST
def sub_comment(request, english_name, comment_id, reply_id):
    article = Article.objects.get(english_name=english_name)
    parent_comment = Comment.objects.get(id=comment_id)
    reply_name = Comment.objects.get(id=reply_id).name
    form = CommentForm(request.POST)
    email = request.POST.get('email')
    QQ = email[:email.find('@')]
    img_url = f'https://q.qlogo.cn/headimg_dl?dst_uin={QQ}&spec=100'
    comment = form.save(commit=False)
    comment.article = article
    comment.img_url = img_url
    comment.reply_name = reply_name
    comment.parent_comment = parent_comment
    comment.save()
    detail_url = request.META.get('HTTP_REFERER') + '#comment-area'
    if email == settings.DEFAULT_EMAIL and request.user.username == settings.DEFAULT_USER:
        comment.img_url = settings.DEFAULT_URL
        comment.save()
    send_sub_comment_email.delay(comment.name, article.title, detail_url, reply_name, parent_comment.text, parent_comment.email, comment.email)
    return redirect(reverse('article:detail', kwargs={'english_name': english_name}))


