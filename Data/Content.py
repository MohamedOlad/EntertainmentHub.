from newsapi import NewsApiClient
import requests
import json
from urllib.request import urlopen 
import urllib.parse

class ApiData:

      # Initialization
      Url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=e24ceee1edde48599edcd6e9e43a93f9'
      Api_Key = NewsApiClient(api_key='e24ceee1edde48599edcd6e9e43a93f9')

      Json_Request = requests.get(Url, Api_Key).json()

   

      Headline_Title = Json_Request['articles'][1]['title']
      Headline_Description = Json_Request['articles'][1]['description']
      Headline_Url = Json_Request['articles'][1]['url']
      Headline_ToImage = Json_Request['articles'][1]['urlToImage']
      Headline_PublishedAt = Json_Request['articles'][1]['publishedAt']
      Headline_Content = Json_Request['articles'][1]['content']


class Tech:

       Url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=e24ceee1edde48599edcd6e9e43a93f9'
       Api_Key = NewsApiClient(api_key='e24ceee1edde48599edcd6e9e43a93f9')

       Json_Request = requests.get(Url, Api_Key).json()

       Tech_Title = Json_Request['articles'][0] ['title']
       Tech_Description = Json_Request['articles'][0] ['description']
       Tech_Url = Json_Request['articles'][0] ['url']
       Tech_ToImage = Json_Request['articles'][0] ['urlToImage']
       Tech_PublishedAt = Json_Request['articles'][0] ['publishedAt']
       Tech_Content = Json_Request['articles'][0] ['content']

class Sports:

      Url = 'https://newsapi.org/v2/top-headlines?sources=espn&apiKey=e24ceee1edde48599edcd6e9e43a93f9'
      Api_Key = NewsApiClient(api_key='e24ceee1edde48599edcd6e9e43a93f9')

      Json_Request = requests.get(Url, Api_Key).json()
       
      Sport_Title = Json_Request['articles'][0] ['title']
      Sport_Description = Json_Request['articles'][0] ['description']
      Sport_Url = Json_Request['articles'][0] ['url']
      Sport_ToImage = Json_Request['articles'][0] ['urlToImage']
      Sport_PublishedAt = Json_Request['articles'][0] ['publishedAt']
      Sport_Content = Json_Request['articles'][0] ['content']

class Entertainment:

       Url = 'https://newsapi.org/v2/top-headlines?sources=the-lad-bible&apiKey=e24ceee1edde48599edcd6e9e43a93f9'
       Api_Key = NewsApiClient(api_key='e24ceee1edde48599edcd6e9e43a93f9')

       Json_Request = requests.get(Url, Api_Key).json()
       
       Entertainment_Title = Json_Request['articles'][0] ['title']
       Entertainment_Description = Json_Request['articles'][0] ['description']
       Entertainment_Url = Json_Request['articles'][0] ['url']
       Entertainment_ToImage = Json_Request['articles'][0] ['urlToImage']
       Entertainment_PublishedAt = Json_Request['articles'][0] ['publishedAt']
       Entertainment_Content = Json_Request['articles'][0] ['content']

       

class Business:

       Url = 'https://newsapi.org/v2/top-headlines?sources=cnbc&apiKey=e24ceee1edde48599edcd6e9e43a93f9'
       Api_Key = NewsApiClient(api_key='e24ceee1edde48599edcd6e9e43a93f9')

       Json_Request = requests.get(Url, Api_Key).json()
       
       Business_Title = Json_Request['articles'][0] ['title']
       Business_Description = Json_Request['articles'][0] ['description']
       Business_Url = Json_Request['articles'][0] ['url']
       Business_ToImage = Json_Request['articles'][0] ['urlToImage']
       Business_PublishedAt = Json_Request['articles'][0] ['publishedAt']
       Business_Content = Json_Request['articles'][0] ['content']


class Mtv:

       Url = 'https://newsapi.org/v2/top-headlines?sources=mtv-news&apiKey=e24ceee1edde48599edcd6e9e43a93f9'
       Api_Key = NewsApiClient(api_key='e24ceee1edde48599edcd6e9e43a93f9')

       Json_Request = requests.get(Url, Api_Key).json()
       
       Mtv_Title = Json_Request['articles'][0] ['title']
       Mtv_Description = Json_Request['articles'][0] ['description']
       Mtv_Url = Json_Request['articles'][0] ['url']
       Mtv_ToImage = Json_Request['articles'][0] ['urlToImage']
       Mtv_PublishedAt = Json_Request['articles'][0] ['publishedAt']
       Mtv_Content = Json_Request['articles'][0] ['content']


class BuzzFeed:

       Url = 'https://newsapi.org/v2/top-headlines?sources=buzzfeed&apiKey=e24ceee1edde48599edcd6e9e43a93f9'
       Api_Key = NewsApiClient(api_key='e24ceee1edde48599edcd6e9e43a93f9')

       Json_Request = requests.get(Url, Api_Key).json()
       
       BuzzFeed_Title = Json_Request['articles'][0] ['title']
       BuzzFeed_Description = Json_Request['articles'][0] ['description']
       BuzzFeed_Url = Json_Request['articles'][0] ['url']
       BuzzFeed_ToImage = Json_Request['articles'][0] ['urlToImage']
       BuzzFeed_PublishedAt = Json_Request['articles'][0] ['publishedAt']
       BuzzFeed_Content = Json_Request['articles'][0] ['content']
     


class Reddit:

       Url = 'https://newsapi.org/v2/top-headlines?sources=reddit-r-all&apiKey=e24ceee1edde48599edcd6e9e43a93f9'
       Api_Key = NewsApiClient(api_key='e24ceee1edde48599edcd6e9e43a93f9')

       Json_Request = requests.get(Url, Api_Key).json()
       
       Reddit_Title = Json_Request['articles'][0] ['title']
       Reddit_Description = Json_Request['articles'][0] ['description']
       Reddit_Url = Json_Request['articles'][0] ['url']
       Reddit_ToImage = Json_Request['articles'][0] ['urlToImage']
       Reddit_PublishedAt = Json_Request['articles'][0] ['publishedAt']
       Reddit_Content = Json_Request['articles'][0] ['content']


