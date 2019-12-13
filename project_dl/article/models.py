from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "article"
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)


class Commands(models.Model):
    class Meta:
        db_table = 'comments'

    comment_text = models.TextField()
    comments_article = models.ForeignKey(Article, on_delete=models.CASCADE)
