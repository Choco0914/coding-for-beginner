from django.db import models

# Create Your models here.
class Article(models.Model):
    """게시글의 모델을 정의해준다."""
    title = models.CharField(max_length=30)
    contents = models.TextField()
    view_count = models.IntegerField()

    def __str__(self):
        """등록되어 있는 모델의 객체를 표시해준다"""
        return '%s %s' % (self.title, self.view_count)

class Comment(models.Model):
    """게시글의 댓글 모델을 정의해준다."""
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
