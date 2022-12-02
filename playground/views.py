from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import date
# Create your views here.

def say_hello(request):
    return render(request, 'hello.html')
def index(request):
    return render(request, 'index.html')
def news(request):
    d=date.today()
    url = f'https://newsapi.org/v2/everything?q=stock&from={d}&sortBy=popularity&apiKey=0957d343be6f4c79b9901b1af0ac60e3'

    crypto_news = requests.get(url).json()

    a = crypto_news['articles']
    desc =[]
    title =[]
    img =[]
    urla=[]
    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        urla.append(f['url'])
    mylist = zip(title, desc, img,urla)

    context = {'mylist': mylist}

    return render(request, 'news.html', context)

def portfoliogenerator(request):
    try:
        print(int(request.POST['name']))
    except:
        print("")
    return render(request, "lpform1.html")
