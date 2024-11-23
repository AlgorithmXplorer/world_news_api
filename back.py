import os
import json
import requests
from colorama import Fore , Style

url = "https://api.worldnewsapi.com/"
api_key = "cead7d36af904c9a9cb91ce0eef816de"
header = {"x-api-key" :api_key}

class news:
    def __init__(self,language , country , time , author, category , url , title , summary):
        self.title = title
        self.country = country
        self.language = language
        self. category = category
        self.summary = summary
        self.url = url
        self.time = time
        self.author = author

    def fore(self,param): 
        new_str = Fore.RED + param + Style.RESET_ALL
        return new_str
    def get_news(self):
        print(self.fore( str(self.title).upper() ), end=f"\n{'*' * (len(self.title)+ 5) }\n")
        #* bu class içinde haber verilerini düzgünce çıktı etmek için bir fonksiyon. bu.
        #todo başlık kısmı hazırlandı. geri kalan kısmı yapmalısın yani yazar ülke dil , url vb bilgileri. 
    

deneme = news(title="wıjdfwıpubefpıvwfuwyv", country="tr",language=None,category=None, summary=None, url=None,time=None,author=None)
deneme.get_news()









