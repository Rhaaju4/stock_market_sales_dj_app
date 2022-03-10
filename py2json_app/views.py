from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.

def str2json(request):
    employee = '{"Id " : " 0000 "," name " : " baba_mohan ", " department " : " saks "}'
    employee_js = json.dumps(employee, indent=4)

    return HttpResponse(employee_js)
"""
def json_reading(request, asd = 1):
    if asd == 1:
        f = open('stock_market_data.json')

        f2 = json.load(f)
        f3 = []
        for i in f2["data"]:
            f3.append(f3)
    return HttpResponse(f3)
"""