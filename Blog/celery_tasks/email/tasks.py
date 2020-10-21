from django.core.mail import send_mail, send_mass_mail
from ..main import celery_app
from Blog.settings import EMAIL_FROM, DEFAULT_EMAIL


@celery_app.task(name='send_comment_email')
def send_comment_email(comment_name, article_title, url):
    html_message = f'<p style="font-size:1.5rem;">{comment_name}评论了{article_title}。详情点击：<a href="{url}">评论</a></p>'
    send_mail('评论回复', '', EMAIL_FROM, [DEFAULT_EMAIL], html_message=html_message)


@celery_app.task(name='send_sub_comment_email')
def send_sub_comment_email(comment_name, article_title, detail_url, reply_name, parent_comment_text, parent_comment_email, comment_email):
    html_message1 = f'{comment_name}评论了{article_title}。详情点击：{detail_url}'
    html_message2 = f'{reply_name}您好!\n{comment_name}在{article_title}中回复了您的评论：{parent_comment_text}。\n详情请点击：{detail_url}'
    message1 = ('评论回复', html_message1, EMAIL_FROM, [DEFAULT_EMAIL])
    message2 = ('评论回复', html_message2, EMAIL_FROM, [parent_comment_email])
    if DEFAULT_EMAIL == comment_email:
        send_mass_mail((message2,))
    else:
        send_mass_mail((message1, message2))

