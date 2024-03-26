from django.db import models

# Create your models here.

'''
1、我们的模型类需要继承　models.Model
2、系统会自动为我们添加一个主键　id
3、字段
    字段名=model.类型（选项）
    字段名其实就是数据表的字段名，字段名不要使用关键字

模型迁移
python manage.py makemigrations     #生成迁移文件
python manage.py migrate            #执行迁移文件

站点管理
站点分为内容发布和公共访问两部分
内容发布的部分由网站的管理员负责查看、添加、修改、删除数据
Django能够根据定义的模型类自动地生成管理模块

使用Django的管理模块，需要按照如下步骤操作：
1、管理界面本地化  (settings.py):
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
2、创建管理员
python manage.py createsuperuser
3、注册模型类  (admin.py):
from book.models import BookInfo,PeopleInfo
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
4、发布内容到数据库  (models.py):
class BookInfo(models.Model):
    ...
    def __str__(self):
        return self.name

'''
class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    #重写str方法让admin后台显示书籍名字
    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    #外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
