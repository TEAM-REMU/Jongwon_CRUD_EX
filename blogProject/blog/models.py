from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # 작성자
    author = models.CharField( max_length=10)
    # 제목
    title = models.CharField(max_length=50)
    # 본문
    body = models.TextField()
    # 작성일
    created_date = models.DateTimeField(default=timezone.now)
    # 수정일
    edited_date = models.DateTimeField(default=timezone.now)

    # 조회수
    visited_count = models.IntegerField()

    # 포스트 작성 함수
    # 글 수정시 수정 시간 자동으로 업데이트 하도록 하는 함수
    def write(self):
        self.edited_date = timezone.now()
        self.save()

    # 포스트를 나타내는 문자열에 제목 반환
    def __str__(self):
        return self.title

    # 해당 글에 방문할 시 조회수 올리고 저장
    def visit(self):
        self.visited_count += 1
        self.save()