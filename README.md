# News Aggregator
An application that aggregates news from two different APIs.
Reddit
News Api

##Installation

I'll recomend using a virtual enviroment for this.

```bash
pip install -r requirements.txt
```
##Running

Use unicorn to run the appn after installing all the libraries

```bash
uvicorn main:app --reload
```
##Routes

I have Divided the whole app routes into basically two types.

###1 : Renders Data directly

Directly returns raw general News data from News Api And Reddit Api
> http://127.0.0.1:8000/
![data:image/png;base64,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]
Directly returns raw News data from News Api And Reddit Api for a particularly searched keyword
> http://127.0.0.1:8000/search?q=football

###2 : Renders Data through WebPage

I have designed a simple webpage for these Routes

Renders Webpage for general News data from News Api And Reddit Api
> http://127.0.0.1:8000/home

Renders Webpage for News data from News Api And Reddit Api for a particularly searched keyword
> http://127.0.0.1:8000/news?q=football

##Design
The entire application depends on four functions named as:

####1: NewsApiReq()
Returns list of general news items as an array from News Api

####2: RedditApiReq()
Returns list of general news items as an array from Reddit Api

####3: NewsSearchApiReq()
Returns list of searched news items as an array from News Api 

####4: RedditearchApiReq()
Returns list of searched news items as an array from Reddit Api

Every route calls two functions one and combines the responses to return as a webpage or raw data.

###Chaching
> I have utilized pythons innbuilt functools.lru_chache to implement chache. I serves the purpose for this simple application without invluding any complex database.

###Adding new API to the Aggregator

######1: Replicate the design of the functions that call that api from the existing serch or general functions. Make sure to iterate through the api response to convert it into a list of dictionaries with headline, link and source as keys, just like existing functions.
######2: In the routes add a call to that function and append the response data to the final array. 

