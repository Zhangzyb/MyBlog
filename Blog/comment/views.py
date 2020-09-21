from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
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
    detail_url = request.META.get('HTTP_REFERER') + '#comment-area'
    html_message = f'<p style="font-size:1.5rem;">{comment_ins.name}评论了{article.title}。详情点击：<a href="{detail_url}">评论</a></p>'
    send_mail('评论回复', '', settings.EMAIL_FROM, [settings.DEFAULT_EMAIL], html_message=html_message)
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
    detail_url = request.META.get('HTTP_REFERER')+'#comment-area'
    html_message1 = f'{comment.name}评论了{article.title}。详情点击：{detail_url}'
    html_message2 = f'{reply_name}您好!\n{comment.name}在{article.title}中回复了您的评论：{parent_comment.text}。\n详情请点击：{detail_url}'
    message1 = ('评论回复', html_message1, settings.EMAIL_FROM, [settings.DEFAULT_EMAIL])
    message2 = ('评论回复', html_message2, settings.EMAIL_FROM, [parent_comment.email])
    send_mass_mail((message1, message2), fail_silently=False)
    return redirect(reverse('article:detail', kwargs={'english_name': english_name}))


