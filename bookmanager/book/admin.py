from django.contrib import admin

# Register your models here.
from book.models import BookInfo,PeopleInfo

#注册模型类(注册后重启)
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)