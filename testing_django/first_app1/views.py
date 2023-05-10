from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me': "Hello im from veiws.py"}
    return render(request,'first_app1\index.html',context = my_dict)  

# Create your views here.
