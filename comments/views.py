from blog.models import Post
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages

from .forms import CommentForm


@require_POST  # 限定为POST请求
def comment(request, post_pk):  # 获取用户submit上来的表单
    post = get_object_or_404(Post, pk=post_pk)  # 判断文章是否存在
    form = CommentForm(request.POST)  # 通过提交的表单数据生成CommentForm实例
    if form.is_valid():  # 数据合法
        comment = form.save(commit=False)  # 生成Comment模型实例，但还不存到数据库
        comment.post = post  # 绑定对应的文章
        comment.save()  # 将数据存进数据库
        messages.add_message(request, messages.SUCCESS, '评论发表成功！', extra_tags='success')
        return redirect(post)  # 重定向到post的get_absolute_url方法返回的url
    # 数据不合法就返回原网址，并且将用户填写的表单返回，同时渲染出需要更改的部分
    context = {
        'post': post,
        'form': form,
    }
    messages.add_message(request, messages.ERROR, '评论发表失败！请修改表单中的错误后重新提交。', extra_tags='danger')
    return render(request, 'comments/preview.html', context=context)
