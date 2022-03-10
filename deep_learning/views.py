from django.http import HttpResponse
from django.shortcuts import render
from deep_learning.models import sale_market_viz
import json
# Create your views here.
def deep_learning2(request):
    dl_algo = ["Convolutional Neural Networks CNNs", "Long Short Term Memory Networks (LSTMs)", "Recurrent Neural Networks (RNNs)", 
    "Generative Adversarial Networks (GANs)", "Radial Basis Function Networks (RBFNs)",
     "Multilayer Perceptrons (MLPs)", "Self Organizing Maps (SOMs)", "Deep Belief Networks (DBNs)"]
    
    dl_list = []
    for i in dl_algo:
        dl_list.append(i)
        print("")
        dl_list.append("** ")
        

    return HttpResponse(dl_list)

#conversion of string to json data
def str2json(request):
    employee = '{"Id " : " 0000 "," name " : " baba_mohan ", " department " : " saks "}'
    employee_js = json.dumps(employee, indent=4)

    return HttpResponse(employee_js)

def data_vizual(request):
    data_viz = sale_market_viz.objects.all()
    return render(request, 'templates/dv.html', {'data_vizua': data_viz})