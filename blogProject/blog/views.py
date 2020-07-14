from django.shortcuts import render
from .models import Post

# 메인 페이지의 포스트를 최신순으로 불러와 템플릿에 전달
def home(request):

    posts = Post.objects.all().order_by('-created_date')

    return render(request, 'home.html', {'posts' : posts})