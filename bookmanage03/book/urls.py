from django.urls import path
from book.views import create_book,shop, register,json,method

from django.urls import converters      #导入转换器模块
from django.urls.converters import register_converter

#1、定义转换器
class MobileConverter:       #根据系统IntConverter转换器自定义手机号验证的转换器
    #验证数据的关键是正则
    regex = '1[3-9]\d{9}'
    #验证没有问题的数据，给视图函数
    def to_python(self, value):
        return int(value)
    # def to_url(self, value):
    #     return str(value)       #将匹配结果用于反向解析传值时使用

#2、注册转换器，才能在第三步中使用
# converters 转换器类
# type_name 转换器名字
register_converter(MobileConverter, 'phone')

urlpatterns = [
    path('create/', create_book),
    # path('<city_id>/<shop_id>', shop),
    # <转换器名字:变量名>　转换器会对变量数据进行正则的验证
    # path('<int:city_id>/<int:shop_id>', shop),
#3、使用自定义转换器
    path('<int:city_id>/<phone:shop_id>', shop),
    path('register/', register),
    path('json/' , json),
    path('method/', method),
]
