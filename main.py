from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import time
import timeit
from functools import lru_cache

app = FastAPI()

#including static files
app.mount("/static", StaticFiles(directory="static"), name="static")

#including templates
templates = Jinja2Templates(directory="templates")

#including headers for authentication
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

#API to search news from News APi
#LRU chace to store 2 recent topic  
@lru_cache(2)
def NewsSearchApiReq(q):
    try:
        x = requests.get('https://newsapi.org/v2/everything?q='+q+'&apiKey=dd97e3a712ef4d4d9f4465c3a5a2abf7')
        json_response = x.json()
        articles =[ {"headline": x["title"], "link":x["url"], "source": "NewsApi"} for x in json_response['articles']]
        return articles
    except:
        return []


#API to search news from Reddit APi
#LRU chace to store 2 recent topic  
@lru_cache(2)
def RedditSearchApiReq(q):
    try:
        reddit = requests.get('https://www.reddit.com/search.json?q='+q,headers=headers)
        json_response = reddit.json()
        articles =[ {"headline": x['data']['title'], "link":x['data']['url'], "source": "Reddit"} for x in json_response['data']['children']]
        return articles
    except:
        return []



#API for general news from News API
def NewsApiReq():
    try:
        x = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=dd97e3a712ef4d4d9f4465c3a5a2abf7')
        json_response = x.json()
        articles =[ {"headline": x["title"], "link":x["url"], "source": "NewsApi"} for x in json_response['articles']]
        return articles
    except:
        return []

#API for general news from News API
def RedditApiReq():
    try:
        reddit = requests.get('https://www.reddit.com/search.json?q=news',headers=headers)
        json_response = reddit.json()
        articles =[ {"headline": x['data']['title'], "link":x['data']['url'], "source": "Reddit"} for x in json_response['data']['children']]
        return articles
    except:
        return[]


#Renders Raw Data

#Renders General News Data from News Api

@app.get("/")
async def root(request:Request):
    
    resNewsApi=NewsApiReq()

    resRedditApi=RedditApiReq()

    res= resNewsApi + resRedditApi

    return res

#Renders General News Data from Reddit Api

@app.get("/search")
async def news(request:Request, q: str = ""):

    resNewsApi=NewsSearchApiReq(q)

    resRedditApi=RedditSearchApiReq(q)

    res= resNewsApi + resRedditApi

    return res

#Renders HTML Pages

#Renders General News
@app.get("/home")
async def root(request:Request):
    
    resNewsApi=NewsApiReq()

    resRedditApi=RedditApiReq()

    res= resNewsApi + resRedditApi

    return templates.TemplateResponse("item.html", {"request": request, "items": res})

#Renders Specific News through search
@app.get("/news")
async def news(request:Request, q: str = ""):

    resNewsApi=NewsSearchApiReq(q)

    resRedditApi=RedditSearchApiReq(q)

    res= resNewsApi + resRedditApi

    return templates.TemplateResponse("item.html", {"request": request, "items": res})
