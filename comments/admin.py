from django.contrib import admin
from .models import Comment


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'post']
    # 创建时间默认更新，不需要显示


admin.site.register(Comment, CommentAdmin)
