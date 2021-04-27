from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from regex_field import models


@require_http_methods(["GET"])
def regex(request):
    a = "["
    print("a: ", a)
    try:
        models.RegularExpression.objects.create(regex=a)
        return HttpResponse('<h1>success request.</h1>')
    except Exception as e:
        print("exception: ", e)
        return HttpResponse('<h1>bad request.</h1>')
