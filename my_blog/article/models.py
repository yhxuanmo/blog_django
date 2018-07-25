from datetime import datetime
from django.db import models


class ArticleTag(models.Model):
    """
    文章分类标签
    """
    tag_name = models.CharField(max_length=32, null=False, unique=True)  # 文章标签
    create_time = models.DateTimeField(auto_now=datetime.now())  # 创建时间
    is_delete = models.BooleanField(default=0)  # 是否禁用

    class Meta:
        db_table = 'tb_article_tag'

    def to_dict(self):
        return {
            'tag_name':self.tag_name,
            'tag_id':self.id
        }



class MyArticle(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=64, null=False)  # 标题
    author = models.CharField(max_length=32, null=False)  # 作者
    abstract = models.CharField(max_length=128, null=False)  # 摘要

    article = models.TextField(null=False)  # 文章
    create_time = models.DateTimeField(auto_now_add=True, null=False)  # 创建时间
    update_time = models.DateTimeField(auto_now=datetime.now(), null=False)  # 更新时间
    count_of_read = models.IntegerField(default=0, null=True)  # 阅读数
    count_of_comment = models.IntegerField(default=0, null=True)  # 评论数
    recommend = models.BooleanField(default=0)  # 推荐
    auditing = models.BooleanField(default=0)  # 审核
    is_show = models.BooleanField(default=0)  # 展示
    tag = models.ForeignKey(ArticleTag)  # 标签

    class Meta:
        db_table = 'tb_article'

    def main_to_dict(self):
        return {
            'id':self.id,
            'title':self.title,
            'author': self.author,
            'abstract':self.abstract,
            'tag': self.tag.tag_name,
            'create_time': self.create_time,
            'count_of_read': self.count_of_read,
            'count_of_comment':self.count_of_comment,
            'recommend':self.recommend,
            'auditing':self.auditing,
            'is_show':self.is_show
        }

    def all_to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'abstract': self.abstract,
            'tag': self.tag.tag_name,
            'article':self.article,
            'create_time': self.create_time,
            'update_time':self.update_time,
            'count_of_read': self.count_of_read,
            'count_of_comment': self.count_of_comment
        }


class ReaderComment(models.Model):
    """
    评论
    """
    reader_name = models.CharField(max_length=32, null=False)  # 评论用户名
    comment_time = models.DateTimeField(auto_now=datetime.now(), null=False)  # 评论时间
    comment = models.TextField(null=False)  # 评论
    head_img = models.CharField(max_length=128) # 评论者头像
    article_id = models.ForeignKey(MyArticle, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tb_reader_comment'


