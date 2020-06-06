from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient
import PIL
import PIL.Image
from datetime import datetime
import COVID19Py
import requests
from bs4 import BeautifulSoup


def Home(request):
    stats = []
    States = []
    Confirmed = []

    def extract_contents(row): return [x.text.replace('\n', '') for x in row]
    URL = 'https://www.mohfw.gov.in/'
    SHORT_HEADERS = ['SNo', 'State', 'Indian-Confirmed',
                     'Foreign-Confirmed', 'Cured',     'Death']
    response = requests.get(URL).content
    soup = BeautifulSoup(response, 'html.parser')
    header = extract_contents(soup.tr.find_all('th'))
    stats = []
    all_rows = soup.find_all('tr')
    for row in all_rows:
        stat = extract_contents(row.find_all('td'))
        if stat:
            stats.append(stat)
    records = stats[36]

    active, Cured, Death, Confirmed = records[2:]
    print(records)
    Confirmed = (Confirmed.split('*')[0])
    Cured = (Cured)
    Death = (Death)
    Active = (active)
    stats = stats[0:35]
    print(stats[1])
    context = {'performance': stats, 'Confirmed': Confirmed,
               'Cured': Cured, 'Death': Death, 'Active': Active}
    return render(request, "Crona/index.html", context)


def MapView(request):
    stats = []
    States = []
    Confirmed = []
    def extract_content(row): return [x.text.replace('\n', '') for x in row]
    URL = 'https://www.mohfw.gov.in/'
    HEADINGS = ['SNO', 'State', 'Indian-Confirmed',
                'Foreign-confirmed', 'Cured', 'Death']
    response = requests.get(URL).content
    soup = BeautifulSoup(response, 'html.parser')
    header = extract_content(soup.tr.find_all('th'))
    all_rows = soup.find_all('tr')
    for row in all_rows:
        stat = extract_content(row.find_all('td'))
        stats.append(stat[1:5])
    stats = stats[0:37]
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
    return render(request, "Crona/mapview.html", {'new_stats': new_stats})


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
