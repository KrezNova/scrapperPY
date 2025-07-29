# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)
#     print(response.status_code)

# scrape_books(url)




# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return
    
#     response.encoding = response.apparent_encoding

#     print(response.text)

# scrape_books(url)





# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return
    
#     response.encoding = response.apparent_encoding
     
#     ''' #  response.text is html and esma chai dherai type ko data 
#     # haru pass garna sakxa ra esma kun type ko data or parser ho vanera vanna parxa so
#     # ani local variable 'soup' is assigned
#     #class ko object banako ho, beautifulsoup vanne class ma data pathaune ani html.parsewr use garne vanera pathaidine
# # so basically, beautifulsoupko object paryo/banyo, so esbata data jhikna milxa resko lagi we do'''

#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")
#     print(books)

# scrape_books(url)





# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return
    
#     response.encoding = response.apparent_encoding
     
#     ''' #  response.text is html and esma chai dherai type ko data 
#     # haru pass garna sakxa ra esma kun type ko data or parser ho vanera vanna parxa so
#     # ani local variable 'soup' is assigned
#     #class ko object banako ho, beautifulsoup vanne class ma data pathaune ani html.parsewr use garne vanera pathaidine
# # so basically, beautifulsoupko object paryo/banyo, so esbata data jhikna milxa resko lagi we do'''

#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")
#     for book in books:
#         title = book.h3.a['title']
#         print(title)
   

# scrape_books(url)



# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return
    
#     response.encoding = response.apparent_encoding
#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")
#     for book in books:
#         title = book.h3.a['title']
#         print(title)
#         price_text = book.find('p', class_='price_color').text
#         print(price_text)

# scrape_books(url)



# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return
    
#     response.encoding = response.apparent_encoding
#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")
#     for book in books:
#         title = book.h3.a['title']
#         print(title)
#         price_text = book.find('p', class_='price_color').text
#         print(price_text, type(price_text))

# scrape_books(url)




# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return
    
#     response.encoding = response.apparent_encoding
#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")
#     for book in books:
#         title = book.h3.a['title']
#         print(title)
#         price_text = book.find('p', class_='price_color').text
#         currency = price_text[0]
#         price = float(price_text[1:])
#         print(title, currency, price)

# scrape_books(url)




# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return
    
#     response.encoding = response.apparent_encoding
#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")

#     book_list = []
#     for book in books:
#         title = book.h3.a['title']
#         print(title)
#         price_text = book.find('p', class_='price_color').text
#         currency = price_text[0]
#         price = float(price_text[1:])
#         book_list.append(
#             {
#                 "title": title,
#                 "currency": currency,
#                 "price": price,
#             }
#         )
#         return(book_list)

# scrape_books(url)




# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return
    
#     response.encoding = response.apparent_encoding
#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")

#     book_list = []
#     for book in books:
#         title = book.h3.a['title']
#         print(title)
#         price_text = book.find('p', class_='price_color').text
#         currency = price_text[0]
#         price = float(price_text[1:])
#         book_list.append(
#             {
#                 "title": title,
#                 "currency": currency,
#                 "price": price,
#             }
#         )
#     print(book_list)

# scrape_books(url)




# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return []
    
#     response.encoding = response.apparent_encoding
#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")

#     book_list = []
#     for book in books:
#         title = book.h3.a['title']
#         print(title)
#         price_text = book.find('p', class_='price_color').text
#         currency = price_text[0]
#         price = float(price_text[1:])
#         book_list.append(
#             {
#                 "title": title,
#                 "currency": currency,
#                 "price": price,
#             }
#         )
#     return book_list

# scrape_books(url)




# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return []
    
#     response.encoding = response.apparent_encoding
#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")

#     book_list = []
#     for book in books:
#         title = book.h3.a['title']
#         print(title)
#         price_text = book.find('p', class_='price_color').text
#         currency = price_text[0]
#         price = float(price_text[1:])
#         book_list.append(
#             {
#                 "title": title,
#                 "currency": currency,
#                 "price": price,
#             }
#         )
#     return book_list

# all_books = scrape_books(url)


# import json

# with open("books.json", "w") as f:
#     json.dump(all_books, f)




# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return []
    
#     response.encoding = response.apparent_encoding
#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")

#     book_list = []
#     for book in books:
#         title = book.h3.a['title']
#         print(title)
#         price_text = book.find('p', class_='price_color').text
#         currency = price_text[0]
#         price = float(price_text[1:])
#         book_list.append(
#             {
#                 "title": title,
#                 "currency": currency,
#                 "price": price,
#             }
#         )
#     return book_list

# all_books = scrape_books(url)


# import json

# with open("books.json", "w") as f:
#     json.dump(all_books, f, indent = 4)
# #this indent = 4 will give spaces among the titles without clustering it in a single line in that {} books.json file, i.e there'wll be 4 line spaces.



# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return []
    
#     response.encoding = response.apparent_encoding
#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")

#     book_list = []
#     for book in books:
#         title = book.h3.a['title']
#         print(title)
#         price_text = book.find('p', class_='price_color').text
#         currency = price_text[0]
#         price = float(price_text[1:])
#         book_list.append(
#             {
#                 "title": title,
#                 "currency": currency,
#                 "price": price,
#             }
#         )
#     return book_list

# all_books = scrape_books(url)


# import json

# with open("books.json", "w", encoding = "utf-8") as f:
#     json.dump(all_books, f, indent = 4, ensure_ascii = False)




# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return []
    
#     response.encoding = response.apparent_encoding
#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")

#     book_list = []
#     for book in books:
#         title = book.h3.a['title']
#         print(title)
#         price_text = book.find('p', class_='price_color').text
#         currency = price_text[0]
#         price = float(price_text[1:])
#         book_list.append(
#             {
#                 "title": title,
#                 "currency": currency,
#                 "price": price,
#             }
#         )
#     return book_list

# all_books = scrape_books(url)


# import json

# with open("books.json", "w", encoding = "utf-8") as f:
#     json.dump(all_books, f, indent = 4, ensure_ascii = False)


# import csv

# with open("books.csv", "w", newline = "", encoding = "utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Title", "Currency", "Price"])
#     for book in all_books:
#         writer.writerow([book["title"], book["currency"], book["price"]])


# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return []
    
#     response.encoding = response.apparent_encoding
#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")

#     book_list = []
#     for book in books:
#         title = book.h3.a['title']
#         print(title)
#         price_text = book.find('p', class_='price_color').text
#         currency = price_text[0]
#         price = float(price_text[1:])
#         book_list.append(
#             {
#                 "title": title,
#                 "currency": currency,
#                 "price": price,
#             }
#         )
#     return book_list

# all_books = scrape_books(url)


# import json

# with open("books.json", "w", encoding = "utf-8") as f:
#     json.dump(all_books, f, indent = 4, ensure_ascii = False)


# import csv

# with open("books.csv", "w", newline = "", encoding = "utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames = ["title", "currency", "price"])
#     writer.writeheader()
#     writer.writerows(all_books)










###################### JUN - 29 ##########################

''' 

go to git bash
git config --global user.name "Kristena Nova"
git config --global user.email "kreznova@gmail.com"

git init
git status => if you want to check what the status of files are
git diff => if you want to check what the changes are
git add .
git commit -m "Your message"
copy paste git code from github

1. change the code
2. git add . 
3. git commit -m "Your message"
4. git push 

'''


# import requests
# from bs4 import BeautifulSoup
# import json
# import csv

# url = "http://books.toscrape.com/"

# def scrape_books(url):
#     response = requests.get(url)     #requests is a library and we are using request library
#     if response.status_code != 200:
#         print("Failed to load page")
#         return []
    
#     response.encoding = response.apparent_encoding
#     soup = BeautifulSoup(response.text, "html.parser")
#     books = soup.find_all("article", class_= "product_pod")

#     book_list = []
#     for book in books:
#         title = book.h3.a['title']
#         print(title)
#         price_text = book.find('p', class_='price_color').text
#         currency = price_text[0]
#         price = float(price_text[1:])
#         book_list.append(
#             {
#                 "title": title,
#                 "currency": currency,
#                 "price": price,
#             }
#         )
#     return book_list

# all_books = scrape_books(url)


# with open("books.json", "w", encoding = "utf-8") as f:
#     json.dump(all_books, f, indent = 4, ensure_ascii = False)


# with open("books.csv", "w", newline = "", encoding = "utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames = ["title", "currency", "price"])
#     writer.writeheader()
#     writer.writerows(all_books)




import requests
import json
import csv


from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)     #requests is a library and we are using request library
    if response.status_code != 200:
        print("Failed to load page")
        return []
    
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_= "product_pod")

    book_list = []
    for book in books:
        title = book.h3.a['title']
        print(title)
        price_text = book.find('p', class_='price_color').text
        currency = price_text[0]
        price = float(price_text[1:])
        book_list.append(
            {
                "title": title,
                "currency": currency,
                "price": price,
            }
        )
    return book_list

all_books = scrape_books(url)


with open("books.json", "w", encoding = "utf-8") as f:
    json.dump(all_books, f, indent = 4, ensure_ascii = False)


with open("books.csv", "w", newline = "", encoding = "utf-8") as f:
    writer = csv.DictWriter(f, fieldnames = ["title", "currency", "price"])
    writer.writeheader()
    writer.writerows(all_books)



