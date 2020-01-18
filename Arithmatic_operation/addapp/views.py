from django.shortcuts import render, redirect
from django.http import HttpResponse

def input(request):
    return render(request, 'addapp/base.html')
def add(request):
    x = int(request.GET['t1'])
    y = int(request.GET['t2'])
    z1 = x+y
    sum = '<strong>The Addition of   ', x, '  and  ', y, '   is  ', z1, '.'
    return HttpResponse(sum)
def sub(request):
    x = int(request.GET['t1'])
    y = int(request.GET['t2'])
    z2 = x-y
    sum = 'The Substraction of   ', x, '  and  ', y, '   is  ', z2, '.'
    return HttpResponse(sum)
def mul(request):
    x = int(request.GET['t1'])
    y = int(request.GET['t2'])
    z3 = x*y
    sum = 'The multiplication of   ', x, '  and  ', y, '   is  ', z3, '.'
    return HttpResponse(sum)
def div(request):
    x = int(request.GET['t1'])
    y = int(request.GET['t2'])
    z4 = x/y
    sum = 'The division of   ', x, '  and  ', y, '   is  ', z4, '.'
    return HttpResponse(sum)
def floor(request):
    x = int(request.GET['t1'])
    y = int(request.GET['t2'])
    z5 = x//y
    sum = 'The floor division of   ', x, '  and  ', y, '   is  ', z5, '.'
    return HttpResponse(sum)

