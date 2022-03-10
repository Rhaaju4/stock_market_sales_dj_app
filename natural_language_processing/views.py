from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def natural_language_processing2(request):
    nlp_algo = ["Support Vector Machines.",
"Bayesian Networks.",
"Maximum Entropy.",
"Conditional Random Field."]

    return HttpResponse(nlp_algo)