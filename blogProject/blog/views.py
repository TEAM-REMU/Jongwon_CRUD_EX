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
    # 작성한 글로 redirect 시켜주는데
    # 그 때 1 증가하므로 0으로 초기 설정
    post.visited_count = 0
    # 모델 저장
    post.save()

    return redirect('/post/' + str(post.id))


# 작성된 글 하나를 렌더하는 함수
def post(request, id):

    # 주어진 id와 일치하는 글을 찾는다
    # 만약 존재하지 않으면 404 에러
    try:
        # 해당 id와 일치하는 글 있는지 확인
        post = Post.objects.get(pk=id)
        # 해당 글 방문 함수 호출
        post.visit()
        # post에 담아서 템플릿에 전달
        return render(request, 'post.html', {'post' : post})
    except Post.DoesNotExist:
        # 해당 글이 존재하지 않으므로 404 페이지 렌더링
        return render(request, '404.html')