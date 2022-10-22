import markdown
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags


# Create your models here.

class Category(models.Model):  # 文章属于的类别
    name = models.CharField(max_length=100)  # 类别名

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):  # 文章的相关标签
    name = models.CharField(max_length=100)  # 标签名

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):  # 一篇文章
    title = models.CharField('标题', max_length=100)  # 文章标题
    body = models.TextField('正文')  # 文章的主体部分，通常是大文本
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('修改时间', null=True)
    excerpt = models.CharField('摘要', max_length=100, blank=True)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        md = markdown.Markdown(extensions=[  # 摘要部分并不需要目录结构
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.excerpt = strip_tags(md.convert(self.body))[:54]  # 去掉html标签
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # 通过reverse函数，根据urls文件中定义的detail的url，返回每篇不同id（pk）的文章对应的url
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def get_category_url(self):  # 通过reverse函数，根据urls文件中定义的detail的url，返回每篇不同id（pk）的文章对应的url
        return reverse('blog:category', kwargs={'pk': self.category})
