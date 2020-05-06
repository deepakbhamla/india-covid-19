from django.shortcuts import render
from newsapi import NewsApiClient
import PIL, PIL.Image
from datetime import datetime
import COVID19Py
# import matplotlib
# from matplotlib import pyplot as plt
import requests
from bs4 import BeautifulSoup
# import numpy as np

    
def Home(request):
    stats = []
    States = []
    Confirmed = []

    extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 
    URL = 'https://www.mohfw.gov.in/'
    SHORT_HEADERS = ['SNo', 'State','Indian-Confirmed', 'Foreign-Confirmed','Cured',     'Death'] 
    response = requests.get(URL).content 
    soup = BeautifulSoup(response, 'html.parser') 
    header = extract_contents(soup.tr.find_all('th')) 
    stats = [] 
    all_rows = soup.find_all('tr') 
    for row in all_rows: 
        stat = extract_contents(row.find_all('td')) 
        if stat: 
            stats.append(stat)
    records =stats[33]
    
    Confirmed, Cured, Death = records[1:]
    Confirmed = int(Confirmed.split('*')[0])
    Cured = int(Cured)
    Death = int(Death)
    stats= stats[0:33]   
    context = {'performance':stats,'Confirmed':Confirmed,'Cured':Cured,'Death':Death}
    return render(request,"Crona/index.html",context)
 
def SubscribeView(request):
    return render(request,"crona/subscribe.html")
   
def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def Subscribe(request):
    sub=Subscribe

def Prevent(request):
    return render(request,"Crona/prevent.html")

def Symptoms(request):
    # Creating empty lists to store data
    stats = []
    States = []
    Confirmed = []
    # Getting the required data
    extract_content = lambda row : [x.text.replace('\n','') for x in row]
    URL = 'https://www.mohfw.gov.in/'
    HEADINGS = ['SNO', 'State','Indian-Confirmed','Foreign-confirmed','Cured','Death']
    response = requests.get(URL).content
    soup  = BeautifulSoup(response,'html.parser')
    header = extract_content(soup.tr.find_all('th'))
    # Data Arrangements ops
    all_rows = soup.find_all('tr')
    for row in all_rows:
        stat = extract_content(row.find_all('td'))
        stats.append(stat[1:3])
    stats = stats[0:34]    
    new_stats = [[i[0].lower(), int(i[1])] for i in stats if len(i) != 0]
    new_stats.pop()
    for i in new_stats:
        if i[0] == 'delhi':
            i[0] = 'nct of delhi'
        if i[0] == 'telengana':
            i[0] = 'telangana'
        if i[0] == 'arunachal pradesh':
            i[0] = 'arunanchal pradesh'
        if i[0] == 'andaman and nicobar islands':
            i[0] == 'andaman and nicobar'
    print(new_stats)   
    return render(request,"Crona/symptoms.html",{'new_stats':new_stats})
    

def About(request):
    return render(request,"Crona/about.html")

def News(request):
    newsapi = NewsApiClient(api_key='ad25ee8229784a7eaaaa655bccd78d20')
    top_headlines = newsapi.get_top_headlines(sources='the-times-of-india')
    articles = top_headlines['articles']
    dates = datetime.now().date()

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)

    return render(request,"Crona/news.html",context={"mylist":mylist,'dates':dates})
