from django.shortcuts import render

# Create your views here.
'''
视图：所谓的视图，其实就是python函数
视图函数有2个要求：
1、视图函数的第一个参数就是接收请求，这个请求其实主是HttpRequest的类对象
2、必须返回一个响应
'''

from django.http import HttpRequest
from django.http import HttpResponse
from book.models import BookInfo

def create_book(request):
    book = BookInfo.objects.create(
        name='test02',
        pub_date='2020-12-12',
        read_count=10
    )
    return HttpResponse('create')

def shop(request,city_id,shop_id):
    return HttpResponse(f'{city_id},{shop_id}')

def register(request):
    data = request.POST
    print(data)             #<QueryDict: {'username': ['mao'], 'password': ['123']}>
    return HttpResponse("FormData")

def json(request):
    body=request.body       #josn数据不能通过request.POST获取数据
    print(body)             #byte类型，b'{\n    "name":"mao",\n    "age":25\n}'
    body_str = body.decode()
    print(body_str)         #返回如下str类型
    """
    {
    "name":"mao",
    "age":25
    }
    """
    # JSON形式的字符串　可以转换为python的字典
    import json
    body_dict = json.loads(body_str)
    print(body_dict)        #{'name': 'mao', 'age': 25}
    ###请求头
    print(request.META)
    print(request.META['SERVER_PORT'])
    return HttpResponse("Json")

def method(request):
    print(request.method)           #POST、GET
    return HttpResponse('method')


