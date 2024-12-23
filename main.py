
from back import *

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

        
x = news_repo()
x.language = "tr"
x.country = "tr"
x.categories_news_provider("politics")
a = news_writter(x.list_of_news)
a.pages()
class panel:

    def __init__(self):
        self.categories = ["Breaking News","Politics News","Technology News","Sports News","Business News","Science News","Culture News", "Entertainment News"]
        self.repo = news_repo






