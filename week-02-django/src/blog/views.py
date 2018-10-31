# from django.http import HttpResponse
from django.shortcuts import render
# from random import randint

def index(request):
    """index는 사이트의 문의 처럼 대문역할을 해준다"""
    # random_number = randint(1, 10)
    # return HttpResponse("Hello, world! {}".format(random_number))
    # return HttpResponse("Hello, world!")
    name = "choco"
    context = {'name':name,}
    return render(request, "blog/index.html", context)
