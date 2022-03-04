from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import schedule
import time
import os.path
import sqlite3

# Create your views here.

def index(request):
    return render(request, 'nondynamic/index.html')

def line(request):
    print('>>>>>>>> static line')
    installation= [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]
    context ={
        'installation': installation
    }
    return render(request, 'nondynamic/line.html', context)

def bar(request):
    print('>>>>>>> static bar')
    installation= [5, 5, 5, 5, 5]
    context ={
        'installation': installation
    }
    return render(request, 'nondynamic/bar.html',context)

def order(request):
    print('>>>> order')

    return render(request, 'nondynamic/order.html')


