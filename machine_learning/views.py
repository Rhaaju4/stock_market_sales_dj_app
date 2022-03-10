from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine_learning2(request):
    ml_algo = [" linear classifiers, support vector machines (SVM), decision trees, k-nearest neighbor, and random forest etc."]
    return HttpResponse(ml_algo)