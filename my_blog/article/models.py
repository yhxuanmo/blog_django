from datetime import datetime
from django.db import models

# Create your models here.
class MyArticle(models.Model):
    title = models.CharField(max_length=64, null=False)
    author = models.CharField(max_length=32, null=False)
    abstract = models.CharField(max_length=128, null=False)
    tag = models.CharField(max_length=32, null=False)
    article = models.TextField(null=False)
    create_time = models.DateTimeField(auto_now_add=True, null=False)
    update_time = models.DateTimeField(auto_now=datetime.now(), null=False)
    count_of_read = models.IntegerField(default=0, null=True)
    count_of_comment = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = 'tb_article'

class ReaderComment(models.Model):
    reader_name = models.CharField(max_length=32, null=False)
    comment_time = models.DateTimeField(auto_now=datetime.now(), null=False)
    comment = models.TextField(null=False)
    head_img = models.CharField(max_length=128)
    article_id = models.ForeignKey(MyArticle, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tb_reader_comment'