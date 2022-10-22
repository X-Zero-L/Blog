# 存放模版标签代码
from django import template
from ..models import Post, Tag, Category

register = template.Library()


# 使用装饰器，表示这是一个类型为inclusion_tag的标签，并且给_recent_posts.html这个模版html文件使用
@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num],
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        # dates方法返回一个列表，元素为每篇文章的创建时间，精确到月，经过去重，desc表示降序
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }
