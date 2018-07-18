from datetime import datetime
from django.db import models

# Create your models here.
class MyArticle(models.Model):
    title = models.CharField(max_length=64, null=False)  # 标题
    author = models.CharField(max_length=32, null=False)  # 作者
    abstract = models.CharField(max_length=128, null=False)  # 摘要
    tag = models.CharField(max_length=32, null=False)  # 标签
    article = models.TextField(null=False)  # 文章
    create_time = models.DateTimeField(auto_now_add=True, null=False)  # 创建时间
    update_time = models.DateTimeField(auto_now=datetime.now(), null=False)  # 更新时间
    count_of_read = models.IntegerField(default=0, null=True)  # 阅读数
    count_of_comment = models.IntegerField(default=0, null=True)  # 评论数

    class Meta:
        db_table = 'tb_article'


    def main_to_dict(self):
        return {
            'id':self.id,
            'title':self.title,
            'author': self.author,
            'abstract':self.abstract,
            'tag': self.tag,
            'create_time': self.create_time,
            'count_of_read': self.count_of_read,
            'count_of_comment':self.count_of_comment
        }

    def all_to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'abstract': self.abstract,
            'tag': self.tag,
            'article':self.article,
            'create_time': self.create_time,
            'update_time':self.update_time,
            'count_of_read': self.count_of_read,
            'count_of_comment': self.count_of_comment
        }


class ReaderComment(models.Model):
    reader_name = models.CharField(max_length=32, null=False)  # 评论用户名
    comment_time = models.DateTimeField(auto_now=datetime.now(), null=False)  # 评论时间
    comment = models.TextField(null=False)  # 评论
    head_img = models.CharField(max_length=128) # 评论者头像
    article_id = models.ForeignKey(MyArticle, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tb_reader_comment'