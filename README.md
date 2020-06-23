# News Aggregator
An application that aggregates news from two different APIs

>Reddit

>News Api

## Installation

I'll recomend using a virtual enviroment for this.

```bash
pip install -r requirements.txt
```
##Running

Use unicorn to run the appn after installing all the libraries

```bash
uvicorn main:app --reload
```
## Routes

I have Divided the whole app routes into basically two types.

### 1 : Renders Data directly

Directly returns raw general News data from News Api And Reddit Api.
> http://127.0.0.1:8000/

Directly returns raw News data from News Api And Reddit Api for a particularly searched keyword.
> http://127.0.0.1:8000/search?q=football

### 2 : Renders Data through WebPage

I have designed a simple webpage for these Routes

Renders Webpage for general News data from News Api And Reddit Api.
> http://127.0.0.1:8000/home

Renders Webpage for News data from News Api And Reddit Api for a particularly searched keyword.
> http://127.0.0.1:8000/news?q=football

## Design
The entire application depends on four functions named as:

#### 1: NewsApiReq()
Returns list of general news items as an array from News Api.

#### 2: RedditApiReq()
Returns list of general news items as an array from Reddit Api.

#### 3: NewsSearchApiReq()
Returns list of searched news items as an array from News Api. 

#### 4: RedditearchApiReq()
Returns list of searched news items as an array from Reddit Api.

Every route calls two functions one and combines the responses to return as a webpage or raw data.

### Chaching
> I have utilized pythons innbuilt functools.lru_chache to implement chache. I serves the purpose for this simple application without invluding any complex database.

### Adding new API to the Aggregator

###### 1: Replicate the design of the functions that call that api from the existing serch or general functions. 
###### 2:Make sure to iterate through the api response to convert it into a list of dictionaries with headline, link and source as keys, just like existing functions.
###### 3: In the routes add a call to that function and append the response data to the final array. 

