from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# 메인 페이지의 포스트를 최신순으로 불러와 템플릿에 전달
def home(request):
    # 포스트를 시간순으로 불러온다
    posts = Post.objects.all().order_by('-created_date')

    # 그리고 home.html에 넘겨준다
    return render(request, 'home.html', {'posts' : posts})

# 글 쓰는 화면 렌더링 함수
def write(request):
    return render(request, 'write.html')

# 글을 데이터베이스에 저장하는 함수
def writePost(request):

    # form으로부터 데이터 얻기
    title = request.POST.get('title')
    author = request.POST.get('author')
    body = request.POST.get('body')

    # 모델 생성 후 데이터 입력
    post = Post()
    post.title = title
    post.author = author
    post.body = body
    post.visited_count = 0
    # 모델 저장
    post.save()

    return redirect('/')


# 작성된 글 하나를 렌더하는 함수
def post(request, id):

    # 주어진 id와 일치하는 글을 찾는다
    # 만약 존재하지 않으면 404 에러
    post = get_object_or_404(Post, pk=id)

    post.visit()

    # post에 담아서 템플릿에 전달
    return render(request, 'post.html', {'post' : post})