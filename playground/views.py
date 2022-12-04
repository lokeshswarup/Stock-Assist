from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import date
import csv
# Create your views here.

def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'indexf.html')
def portfoliobw(request):

    file=open(file="bw.csv")
    read=csv.reader(file)
    i0=[]
    i1=[]
    i2=[]
    i3=[]
    i4=[]
    i5=[]
    i6=[]
    i7=[]
    i8=[]
    i9=[]
    i10=[]

    for i in read:
        i0.append(i[0])
        i1.append(i[1])
        i2.append(i[2])
        i3.append(i[3])
        i4.append(i[4])
        i5.append(i[5])
        i6.append(i[6])
        i7.append(i[7])
        i8.append(i[8])
        i9.append(i[9])
        i10.append(i[10])
    mylist = zip(i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10)

    context = {'mylist':mylist}
        
    return render(request,'d.html',context)
def portfolioccp(request):

    file=open(file="ccp.csv")
    read=csv.reader(file)
    i0=[]
    i1=[]
    i2=[]
    i3=[]
    i4=[]
    i5=[]
    i6=[]
    i7=[]
    i8=[]
    i9=[]
    i10=[]

    for i in read:
        i0.append(i[0])
        i1.append(i[1])
        i2.append(i[2])
        i3.append(i[3])
        i4.append(i[4])
        i5.append(i[5])
        i6.append(i[6])
        i7.append(i[7])
        i8.append(i[8])
        i9.append(i[9])
        i10.append(i[10])
    mylist = zip(i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10)

    context = {'mylist':mylist}
        
    return render(request,'d.html',context)
def portfoliofii(request):

    file=open(file="fii.csv")
    read=csv.reader(file)
    i0=[]
    i1=[]
    i2=[]
    i3=[]
    i4=[]
    i5=[]
    i6=[]
    i7=[]
    i8=[]
    i9=[]
    i10=[]

    for i in read:
        i0.append(i[0])
        i1.append(i[1])
        i2.append(i[2])
        i3.append(i[3])
        i4.append(i[4])
        i5.append(i[5])
        i6.append(i[6])
        i7.append(i[7])
        i8.append(i[8])
        i9.append(i[9])
        i10.append(i[10])
    mylist = zip(i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10)

    context = {'mylist':mylist}
        
    return render(request,'d.html',context)
def portfoliol(request):

    file=open(file="l.csv")
    read=csv.reader(file)
    i0=[]
    i1=[]
    i2=[]
    i3=[]
    i4=[]
    i5=[]
    i6=[]
    i7=[]
    i8=[]
    i9=[]
    i10=[]

    for i in read:
        i0.append(i[0])
        i1.append(i[1])
        i2.append(i[2])
        i3.append(i[3])
        i4.append(i[4])
        i5.append(i[5])
        i6.append(i[6])
        i7.append(i[7])
        i8.append(i[8])
        i9.append(i[9])
        i10.append(i[10])
    mylist = zip(i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10)

    context = {'mylist':mylist}
        
    return render(request,'d.html',context)
    
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
