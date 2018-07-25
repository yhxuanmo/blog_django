from datetime import datetime

from django.db import models

# Create your models here.
class User(models.Model):
    """
    用户表
    """
    rel_name = models.CharField(max_length=32,null=True)  # 真实姓名
    user_name = models.CharField(max_length=64, null=False, unique=True)  # 用户名
    passwd = models.CharField(max_length=32,null=False)  # 密码
    sex = models.IntegerField(default=1,null=False)  # 性别
    phone = models.CharField(max_length=11, unique=True,null=True)  # 手机号
    birth = models.DateTimeField(null=False)  # 生日
    position = models.CharField(max_length=128,null=False)  # 地址
    likes = models.CharField(max_length=64,null=True)  # 爱好
    head_img = models.ImageField(null=True)  # 头像
    user_tag = models.CharField(max_length=64,null=True)  # 用户标签
    abstract = models.CharField(max_length=128,null=True)  # 简介
    qq_num = models.CharField(max_length=32, null=True,unique=True)  # qq
    email = models.CharField(max_length=32,null=False,unique=True)  # 邮箱
    weibo = models.CharField(max_length=32,null=True,unique=True)  # 微博
    git_name = models.CharField(max_length=32,null=True, unique=True)  # git账号

    class Meta:
        db_table = 'tb_user'

class WebInfo(models.Model):
    """
    网站信息表
    """
    name = models.CharField(max_length=64,null=False)  # 网站名
    tag = models.CharField(max_length=64,null=False)  # 网站标签
    img = models.ImageField(null=False)  # 网站图标
    web_url = models.CharField(max_length=32,null=False)  # 首页url
    abstract = models.CharField(max_length=128,null=True)  # 网站简介

    class Meta:
        db_table = 'tb_web_info'


class Message(models.Model):
    """
    留言表
    """
    head_img = models.ImageField()  # 头像
    user_name = models.CharField(max_length=64,null=False)  # 用户名
    content = models.TextField(null=False)  # 评论内容
    create_time = models.DateTimeField(auto_now_add=datetime.now())  # 评论时间

    class Meta:
        db_table = 'tb_message'


class MessageReply(models.Model):
    """
    回复留言表
    """
    head_img = models.ImageField()  # 头像
    user_name = models.CharField(max_length=64, null=False)  # 用户名
    content = models.TextField(null=False)  # 回复内容
    create_time = models.DateTimeField(auto_now_add=datetime.now())  # 回复时间
    message = models.ForeignKey(Message)  # 关联评论

    class Meta:
        db_table = 'tb_message_reply'
