from django.db import models

# Create your models here.

class BookInfo(models.Model):
    name = models.CharField(max_length=10,unique=True)
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)
    # 一对双的关系模型中，系统会自动添加一个　关联模型类名小写_set
    # peopleinfo_set = [PeopleInfo,PeopleInfo,...]

    class Meta:
        db_table = 'bookinfo'       #修改表的名字
        verbose_name = '书籍管理'     #admin站点使用的(了解)

    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )
    name = models.CharField(max_length=10,unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE,default=1)
    description = models.CharField(max_length=100,null=True)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    # book = BookInfo()

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name
