from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),

]
#  <a href="{% url 'blog:archive' date.year date.month %"> 解析在urls文件中对应的url模式，然后替换year，month值
# html中做的是得到符合要求的url地址，而实际上地址和对应的view是先存在的
