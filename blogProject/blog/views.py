from django.shortcuts import render
from .models import Post

# 메인 페이지의 포스트를 최신순으로 불러와 템플릿에 전달
def home(request):
    # 포스트를 시간순으로 불러온다
    posts = Post.objects.all().order_by('-created_date')

    # 그리고 home.html에 넘겨준다
    return render(request, 'home.html', {'posts' : posts})