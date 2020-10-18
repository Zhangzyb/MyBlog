from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField('昵称', max_length=100)
    email = models.EmailField('QQ邮箱')
    text = models.TextField('正文')
    img_url = models.CharField('头像', max_length=100, null=True)
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    article = models.ForeignKey('article.Article', verbose_name='文章', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='父级评论')
    reply_name = models.CharField('回复名称', max_length=100, null=True)

    class Meta:
        ordering = ['-created_time']
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name}: {self.text[:20]}'