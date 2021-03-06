import markdown
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.html import strip_tags
from mdeditor.fields import MDTextField


class Category(models.Model):
    name = models.CharField('分类', max_length=50)
    cate_name = models.CharField('英文名', max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subdir', verbose_name='上级目录')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题',max_length=200)
    english_name = models.CharField('英文名', max_length=100)
    text = MDTextField('正文')
    image = models.ImageField(upload_to='img/%Y/%m/%d')
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('修改时间')
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    abstract = models.CharField('摘要', max_length=1000)
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0, editable=False)
    likes = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.abstract = strip_tags(md.convert(self.text))[:200]
        super().save(*args, **kwargs)

    def inc_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def inc_likes(self):
        self.likes += 1
        self.save(update_fields=['likes'])


class PostLikes(models.Model):
    ip_address = models.CharField('IP地址', max_length=10)
    post = models.ManyToManyField(Article, verbose_name='文章')

    class Meta:
        verbose_name = '点赞'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip_address



