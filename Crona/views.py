from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient
import PIL
import PIL.Image
from datetime import datetime
import COVID19Py
import requests
from bs4 import BeautifulSoup
'''
    url = 'https://api.covid19india.org/data.json'
    response = requests.get(url)
    user = response.json()
    for data in user['statewise']:
        print(f"{data['state']} {data['active']}")
'''

def Home(request):
    state = []
    confirmed = []
    recovered = []
    deaths = []
    active = []
    url = 'https://api.covid19india.org/data.json'
    response = requests.get(url)
    user = response.json()
    for data in user['statewise']:
        state.append(data['state'])
        confirmed.append(data['confirmed'])
        active.append(data['active'])
        recovered.append(data['recovered'])
        deaths.append(data['deaths'])
    stats = zip(state[1:],confirmed[1:],active[1:],recovered[1:],deaths[1:])
    ttl = confirmed[0]
    act = active[0]
    cur = recovered[0] 
    de = deaths[0]    
    context = {'performance': stats,'ttl':ttl, 'act':act, 'cur':cur, 'de':de}
    return render(request, "Crona/index.html", context)


def MapView(request):
    state = []
    confirmed = []
    recovered = []
    deaths = []
    active = []
    url = 'https://api.covid19india.org/data.json'
    response = requests.get(url)
    user = response.json()
    for data in user['statewise']:
        state.append(data['state'])
        confirmed.append(data['confirmed'])
        active.append(data['active'])
        recovered.append(data['recovered'])
        deaths.append(data['deaths'])

    maps = list(map(list, zip(state,confirmed)))
    new_stats = [[i[0].lower(), int(i[1])] for i in maps if len(i) != 0]
    
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
    return render(request, "Crona/mapview.html",{'new_stats': new_stats} )


def News(request):
    newsapi = NewsApiClient(api_key='ad25ee8229784a7eaaaa655bccd78d20')
    top_headlines = newsapi.get_top_headlines(sources='the-times-of-india')
    articles = top_headlines['articles']
    dates = datetime.now().date()

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]
        url.append(myarticles['url'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img, url)
    return render(request, "Crona/news.html", context={"mylist": mylist, 'dates': dates})
