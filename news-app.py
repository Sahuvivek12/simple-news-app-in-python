import credentials 
import requests
from newsapi import NewsApiClient
api = NewsApiClient(api_key=credentials.API_Key)

l = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
i = int(input("What news do you want to read, \n0 for buisness news, \n1 for entertainment news, \n2 for general news, \n3 for health news, \n4 for science news, \n5 for sports news, \n6 for technology news\n:-"))
r = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&category={l[i]}&apiKey={credentials.API_Key}')
data = r.json()
articles = data['articles']


for article in articles:
        print(f"News: {article['title']}")
        print(f"Read more: {article['url']}")
        print("*" * 50)
