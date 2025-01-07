
from back import *
from bs4 import BeautifulSoup
class news_writter:
    """
    self.list: News received from the user is assigned to this list.
    self.page_index: A counter that tracks which page is being displayed (default is 0).
    """
    def __init__(self,news_list):
        self.list = news_list
        self.page_index = 0

    """
    Prints each item in the specified list to the screen
    """
    def writer(self,liste):
        for i in liste:
            i.get_news()
        print(("*"*40 + "\n" )*4)
    """
    Provides a mechanism to display the news list 'page by page
    """
    def pages(self):
        page_list = page_creater(self.list)
        any_page = page_list[self.page_index]
        self.writer(any_page)

        def inner():

            """
            When the end of the page is reached, the following options are presented to the user:

            n: Moves to the next page (does nothing if it doesn't exist).
            p: Goes back to the previous page.
            e: Exits.
            """
            while True:
                if  0< self.page_index< len(page_list) -1 :
                    print(Style.BRIGHT + Fore.BLUE + f"PAGE: {str(self.page_index + 1)}" + Style.RESET_ALL)
                    choice = input("next page(n) Previous page(p) or exit(e): ").lower().strip()
                    if choice != "n" and choice != "p" and choice != "e":
                        print("please choose properly") 
                    else:
                        return choice
                else:
                    break
            
            """
            If you are on the first page, only the 'move forward (n)' or 'exit (e)' options are offered.
            """            
            while True:
                if self.page_index == 0:
                    print(Style.BRIGHT + Fore.BLUE + f"PAGE: {str(self.page_index + 1)}" + Style.RESET_ALL)
                    choice = input("next page(n) or exit(e): ").lower().strip()
                    if choice != "n" and  choice != "e":
                        print("please choose properly")
                    else:
                        return choice
                else:
                    break
            
            """
            If you are on the last page, only the 'go back (p)' or 'exit (e)' options are offered
            """            
            while True:
                if self.page_index == len(page_list) -1 :
                    print(Style.BRIGHT + Fore.BLUE + f"PAGE: {str(self.page_index + 1)}" + Style.RESET_ALL)
                    choice = input("Previous page(p) or exit(e): ").lower().strip()
                    if choice != "p" and choice != "e":
                        print("please choose properly") 
                    else:
                        return choice

                else:
                    break
        
        """
        Kullanıcı inner() fonksiyonuyla bir seçim yaptıktan sonra:
        Eğer n seçtiyse, bir sonraki sayfaya geçilir.
        Eğer p seçtiyse, bir önceki sayfaya geri gidilir.
        Eğer e seçtiyse, döngü kırılır ve program sonlanır.
        """
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
        self.getting_operation()
        if self.choice == "f":
            self.set_filters()
        
        elif self.choice == "1":
            self.set_populer_news()
        
        elif self.choice == "2":
            self.set_Politics()
        
        elif self.choice == "3":
            self.set_Technology_News()
        
        elif self.choice == "4":
            self.set_Sports_News()
        
        elif self.choice == "5":
            self.set_business()

        elif self.choice == "6":
            self.set_science()
        
        elif self.choice == "7":
            self.set_culture()
        
        elif self.choice == "8":
            self.set_entertainment()
        
        elif self.choice == "9":
            self.search_news()
        
        elif self.choice == "e":
            print("Exit completed")
    
    
    def set_filters(self):
        def language():
            url = "https://worldnewsapi.com/docs/language-codes/"
            header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
            html_codes = requests.get(url=url,headers=header).content
            soup = BeautifulSoup(html_codes,"html.parser")
            languages = soup.find("div",{"id":"apiDocRightSide"}).find_all("td")
            list_short_language = [x.text for x in languages if len(x.text) == 2]
            list_long_language = [x.text for x in languages if len(x.text) > 2]
            return [list_long_language,list_short_language]
        def country():
            url = "https://worldnewsapi.com/docs/country-codes/"
            header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
            html_codes = requests.get(url=url,headers=header).content
            soup = BeautifulSoup(html_codes,"html.parser")
            countrys = soup.find("div",{"id":"apiDocRightSide"}).find_all("td")
            list_short_country = [x.text for x in countrys if len(x.text) == 2]
            list_long_country = [x.text for x in countrys if len(x.text) > 2]
            return [list_long_country,list_short_country]        
        list_language =  language()
        list_country = country()
        while True:
            choice = input("1-language\n2-country\n3-earliest publish date\n4-author\nwhich filter will be changed: ")
            if choice =="1" :
                for name,value in zip(list_language[0],list_language[1]):
                    print(f"{name}- {value}")
                language = input("language(short form, like en ): ")
                if language in list_language[1]:
                    self.repo.language = language
                else:
                    print("there is not a language like this")
                    continue
                break
            
            elif choice == "2":
                for name,value in zip(list_country[0],list_country[1]):
                    print(f"{name}- {value}")
                country = input("country(short form, like us ): ")
                if country in list_country[1]:
                    self.repo.country = country
                else:
                    print("there is not a country like this")
                    continue
                
                break
            
            elif choice == "3":
                date = input("date(2020/2025-1/12-1/31)(clear:c): ")
                if date == "c":
                    self.repo.date = ""
                else:
                    self.repo.date = date
                break
            elif choice == "4":
                author = input("Author(clear:c): ")
                if author == "c":
                    self.repo.author = ""
                else:
                    self.repo.author = author.title()
                break
            else:
                print("please fill the space correctly".center(50,"*"))
        
        self.main()
                
    def set_populer_news(self):
        while True:
            try :
                list_of_news = get_top_news(self.repo)
                writer_func = news_writter(list_of_news)
                writer_func.pages()
            except IndexError:
                print("There is no news about this filters")
                break
            else:
                break
        self.main()
        

    def set_Technology_News(self):
        while True:
            try:
                self.repo.categories_news_provider("technology")
                writer_func = news_writter(self.repo.list_of_news)
                writer_func.pages()
                
            except IndexError:
                print("There is no news about this filters")
                break
            else:
                break
        self.main()

    def set_Politics(self):
        while True:
            try:
                self.repo.categories_news_provider("politics")
                writer_func = news_writter(self.repo.list_of_news)
                writer_func.pages()
                
            except IndexError:
                print("There is no news about this filters")
                break
            else:
                break
        self.main()
        
    def set_entertainment(self):
        while True:
            try:
                self.repo.categories_news_provider("entertainment")
                writer_func = news_writter(self.repo.list_of_news)
                writer_func.pages()
                
            except IndexError:
                print("There is no news about this filters")
                break
            else:
                break
        self.main()
        
    def set_culture(self):
        while True:
            try:
                self.repo.categories_news_provider("culture")
                writer_func = news_writter(self.repo.list_of_news)
                writer_func.pages()
                
            except IndexError:
                print("There is no news about this filters")
                break
            else:
                break
        self.main()
        
    def set_science(self):
        while True:
            try:
                self.repo.categories_news_provider("science")
                writer_func = news_writter(self.repo.list_of_news)
                writer_func.pages()
                
            except IndexError:
                print("There is no news about this filters")
                break
            else:
                break
        self.main()
        
    def set_business(self):
        while True:
            try:
                self.repo.categories_news_provider("business")
                writer_func = news_writter(self.repo.list_of_news)
                writer_func.pages()
                
            except IndexError:
                print("There is no news about this filters")
                break
            else:
                break
        self.main()
        
    def set_Sports_News(self):
        while True:
            try:
                self.repo.categories_news_provider("sports")
                writer_func = news_writter(self.repo.list_of_news)
                writer_func.pages()
                
            except IndexError:
                print("There is no news about this filters")
                break
            else:
                break
        self.main()
        
    def search_news(self):
        while True:
            try :
                self.repo.text = input("news title or News subject(exit:e): ")
                if self.repo.text =="e":
                    raise IndexError
                    
                self.repo.list_of_news = search_news(self.repo, self.repo.text)
                writer_func = news_writter(self.repo.list_of_news)
                writer_func.pages()

            except IndexError:
                print("There is no news about this title")
                break
            else:
                break
        self.main()



x = panel()
x.main()