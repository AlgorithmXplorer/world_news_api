
from back import *
from bs4 import BeautifulSoup
class news_writter:
    def __init__(self,news_list):
        self.list = news_list
        self.page_index = 0

    def writer(self,liste):
        for i in liste:
            i.get_news()
        print(("*"*40 + "\n" )*4)

    def pages(self):
        page_list = page_creater(self.list)
        any_page = page_list[self.page_index]
        self.writer(any_page)
        def inner():
            while True:
                if  0< self.page_index< len(page_list) -1 :
                    print(Style.BRIGHT + Fore.BLUE + f"PAGE: {str(self.page_index + 1)}" + Style.RESET_ALL)
                    choice = input("next page(n) Previous page(p) or exit(e): ").lower().strip()
                    if choice != "n" and choice != "p" and choice != "e":
                        print(choice)
                        raise ValueError("please choose properly") 
                    else:
                        return choice

                else:
                    break
                
            while True:
                if self.page_index == 0:
                    print(Style.BRIGHT + Fore.BLUE + f"PAGE: {str(self.page_index + 1)}" + Style.RESET_ALL)
                    choice = input("next page(n) or exit(e): ").lower().strip()
                    if choice != "n" and  choice != "e":
                        raise ValueError("please choose properly")
                    else:
                        return choice
                else:
                    break
            while True:
                if self.page_index == len(page_list) -1 :
                    print(Style.BRIGHT + Fore.BLUE + f"PAGE: {str(self.page_index + 1)}" + Style.RESET_ALL)
                    choice = input("Previous page(p) or exit(e): ").lower().strip()
                    if choice != "p" and choice != "e":
                        raise ValueError("please choose properly") 
                    else:
                        return choice

                else:
                    break
        
        while True:
            choice = inner()
            print(("*"*40 + "\n" )*10)
            if choice == "n":
                self.page_index += 1
                any_page = page_list[self.page_index]
                self.writer(any_page)
                
            
            elif choice == "p":
                self.page_index -= 1
                any_page = page_list[self.page_index]
                self.writer(any_page)
            elif choice == "e":
                break

        
# x = news_repo()
# x.language = "en"
# x.country = "us"
# x.categories_news_provider("politics")
# a = news_writter(x.list_of_news)
# a.pages()
class panel:
    def __init__(self):
        self.categories = ["Breaking News","Politics News","Technology News","Sports News","Business News","Science News","Culture News", "Entertainment News","news search (title and or News subject)"]
        self.repo = news_repo()
        self.choice = "e"
    
    def getting_operation(self):
        print(f"filtrs ; language:{self.repo.language} // country:{self.repo.country} // date:{self.repo.date} // authors:{self.repo.author}")
        print("categories:")
        for index,i in enumerate(self.categories,1):
            print(f"\t{index}- get {i}")
        numbers = list(range(1,10))
        str_func = lambda x: str(x)
        new_numbers = list(map(str_func, numbers))
        while True:
            try:
                choice = input("choice(filters:f / categories:(numbers) / exit:e): ").lower().strip()
                if choice in new_numbers or choice == "f" or choice == "e":
                    self.choice = choice
                else:
                    raise ValueError("please fill in the space correctly")
            except ValueError as error:
                print(error)
            else:
                break

    def main(self):
        #* burası chice attribute'una göre çalıştıırlcak fonksiyonların yeri
        pass
    def set_filters(self):
        def language():
            url = "https://worldnewsapi.com/docs/language-codes/"
            header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
            html_codes = requests.get(url=url,headers=header).content
            soup = BeautifulSoup(html_codes,"html.parser")
            languages = soup.find("div",{"id":"apiDocRightSide"}).find_all("td")
            list_language = [x.text for x in languages if len(x.text) == 2]
            return list_language
        def country():
            url = "https://worldnewsapi.com/docs/country-codes/"
            header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
            html_codes = requests.get(url=url,headers=header).content
            soup = BeautifulSoup(html_codes,"html.parser")
            countrys = soup.find("div",{"id":"apiDocRightSide"}).find_all("td")
            list_country = [x.text for x in countrys if len(x.text) == 2]
            return list_country        
        list_language =  language()
        list_country = country()
        while True:
            choice = input("1-language\n2-country\n3-earliest publish date\n4-author\nwhich filter will be changed: ")
            if choice =="1" :
                language = input("language(short form, like en ): ")
                if language in list_language:
                    self.repo.language = language
                else:
                    print("there is not a language like this")
                    continue
                break
            
            elif choice == "2":
                country = input("country(short form, like us ): ")
                if country in list_country:
                    self.repo.country = country
                else:
                    print("there is not a country like this")
                    continue
                
                break
            
            elif choice == "3":
                date = input("date(2020/2025-1/12-1/31): ")
                self.repo.date = date
                break
            elif choice == "4":
                author = input("Author: ").title()
                self.repo.author = author
                break
            else:
                print("please fill the space correctly".center(50,"*"))
        
        self.main()
                
    def set_populer_news(self):
        pass
    def set_Technology_News(self):
        pass
    def set_(self):
        pass
    def set_Politics(self):
        pass
    def set_entertainment(self):
        pass
    def set_culture(self):
        pass
    def set_science(self):
        pass
    def set_business(self):
        pass
    def set_Sports_News(self):
        pass
    def search_news(self):
        pass

#todo panelde kullanıcının girdiği işleme göre main içinde fonksiyon çalıştırılıcak. 
#todo her haberin kendi bir sistemi olduğu için her biri farklı fonksiyon
x = panel()
# x.getting_operation()

x.set_filters()

