from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from .forms import CommentForm
from article.models import Article
from .models import Comment


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
    return redirect(reverse('article:detail', kwargs={'english_name': english_name}))


@require_POST
def sub_comment(request, english_name, comment_id, reply_id):
    article = Article.objects.get(english_name=english_name)
    parent_comment = Comment.objects.get(id=comment_id)
    reply_name = Comment.objects.get(id=reply_id).name
    form = CommentForm(request.POST)
    QQ = request.POST.get('email')
    QQ = QQ[:QQ.find('@')]
    img_url = f'https://q.qlogo.cn/headimg_dl?dst_uin={QQ}&spec=100'
    comment = form.save(commit=False)
    comment.article = article
    comment.img_url = img_url
    comment.reply_name = reply_name
    comment.parent_comment = parent_comment
    comment.save()
    return redirect(reverse('article:detail', kwargs={'english_name': english_name}))


