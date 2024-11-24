import os
import json
import requests
from colorama import Fore , Style



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

    def fore(self,choice,param):
        if choice == 1:    
            new_str = Style.BRIGHT + Fore.RED + param + Style.RESET_ALL
            return new_str
        elif choice == 2:    
            new_str = Style.BRIGHT + Fore.BLUE + param + Style.RESET_ALL
            return new_str
    
    def get_news(self):
        print(self.fore( choice=1 , param=str(self.title) ))
        print(f"-{self.summary}")
        print(f"Authored by {self.author}".upper())
        print(f"url: {self.fore( choice=2 , param=str(self.url))}")

#* repo class'ı bir kategori için alınan tüm haberleri kapsayan bir depo.
#* bu class ile oluşturulan bir obje içerisinde belli bir kategoride olan haberleri içericek
class news_repo:
    def __init__(self):
        self.url = "https://api.worldnewsapi.com/"
        self.api_key = "cead7d36af904c9a9cb91ce0eef816de"
        self.header = {"x-api-key" : self.api_key}
        self.news = []


def news_provider(url):
    repo = news_repo()
    response = requests.get(url=url,headers=repo.header)
    #todo bu fonksiyon aldığı url bilgisi ile 100 tane haber alıcak ve aldığı her haberi bir hbaer objesine çevirip
    #todo repo içinde bulunan liste atttribute içine atıcak

deneme = news(title="wıjdfwıpubefpıvwfuwyv", country="tr",language="en",category="sports", summary="aaaa", url="https://xc.com",time=None,author="mustafa")
deneme.get_news()


news_provider("https://api.worldnewsapi.com/search-news?text=politics&country=us&number=20")




