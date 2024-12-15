import os
import json
import requests
from colorama import Fore , Style



class news:

    def __init__(self,language , country , time , author, category , url , title , summary):
        """
        This class serves as a structure to hold data related to news articles.
        It stores basic attributes such as title, country, time, author, category, URL, and summary for each news article.

        Explanation:
        __init__(...): Initializes the news object with the required information like title, country, time, author, category, url, and summary.

        Example: self.title stores the news title, while self.url stores the URL of the news.
        """

        self.title = title
        self.country = country
        self.language = language
        self. category = category
        self.summary = summary
        self.url = url
        self.time = time
        self.author = author

    def font_color(self,choice,param):
        """
        This function returns the given parameter in a specified color based on the choice provided.

        Explanation:

        The choice parameter determines the color (1 for red, 2 for blue).
        The param is the text to be colored.
        Example: font_colorize(1, "Warning") returns the text "Warning" in red color.
        """
        
        if choice == 1:    
            new_str = Style.BRIGHT + Fore.RED + param + Style.RESET_ALL
            return new_str
        elif choice == 2:    
            new_str = Style.BRIGHT + Fore.BLUE + param + Style.RESET_ALL
            return new_str
        
    
    def get_news(self):
        """
        This function prints the parameters of the news class.

        Explanation:
        It displays the class parameters in a readable format.
        It uses the font_colorize function to print colored text.
        Example: It prints title and country information in colored format.
        """
       
        print(self.font_color( choice=1 , param=str(self.title) ))
        print(f"-{self.summary}")
        print(f"Authored by {self.author}".upper())
        print(f"url: {self.font_color( choice=2 , param=str(self.url))}")
        


class news_repo:
    
    def __init__(self):
        """
        This class handles the process of fetching news from an API.

        Explanation:
        __init__(self): Sets up default parameters (language, country, category, etc.) required by the news provider.
        self.api_key holds the key needed to make API requests.
        Example: self.website_url represents the main URL, and self.language represents the query language.
        """
       
        self.language = "en"
        self.country = "us"
        self.date = ""
        self.author = ""
        self.categorie = "science"
        self.text = "science"

        self.website_url = "https://api.worldnewsapi.com"
        self.api_key = "cead7d36af904c9a9cb91ce0eef816de"
        self.header = {"x-api-key" : self.api_key}
        self.list_of_news = []

    def categories_news_provider(self):
        #* the inner function sets the website URL based on what is choice because both the title attributes and categories attributes brings different results
        def inner(choice):
            if choice == 1:    
                if self.date == "":
                    website_url = self.website_url + f"/search-news?categories={self.categorie}&language={self.language}&country={self.country}&author={self.author}&number=50"
                else:
                    website_url = self.website_url + f"/search-news?categories={self.categorie}&language={self.language}&country={self.country}&earliest-publish-date={self.date}&author={self.author}&number=50"
            elif choice == 2:
                if self.date == "":
                    website_url = self.website_url + f"/search-news?text={self.text}&language={self.language}&country={self.country}&author={self.author}&number=50"
                else:
                    website_url = self.website_url + f"/search-news?text={self.text}&language={self.language}&country={self.country}&earliest-publish-date={self.date}&author={self.author}&number=50"
            return website_url
        news_list = []
        def inner_2(URL):
            response = requests.get(url=URL,headers=self.header)
            response = json.loads(response.text)
            
            for index,i in enumerate(response["news"]):
                news = self.news_maker(i)
                news_list.append(news)
        inner_2(inner(1))
        inner_2(inner(2))
        self.list_of_news = news_list
            


    def news_maker(self,news_dicti):
        """
        This function creates a news object using the data provided as a dictionary.

        Explanation:
        
        It processes the news_dict parameter containing news data.
        Returns a news object if successful, or None in case of an error.
        Example: Returns a news object if the dictionary contains author and title, otherwise raises an error.
        
        """
        my_news = news_dicti
        def inner(attrubte):
            try:
                param = my_news[attrubte]
            except KeyError:
                param = ""
            return param
                

        news_author = inner("authors")
        news_title = inner("title")
        news_time = inner("publish_date")
        news_url = inner("url")
        news_summary = inner("summary")
        news_category = inner("category")
        news_language = inner("language")
        news_country = inner("source_country")
        new_news = news(language=news_language , country= news_country ,time = news_time , author= news_author , category= news_category , url= news_url , title= news_title , summary= news_summary )
        return new_news


x = news_repo()
x.categories_news_provider()
print(len(x.list_of_news))





