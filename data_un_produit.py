import requests
from bs4 import BeautifulSoup
import csv


url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
#urls = ['https://books.toscrape.com/catalogue/page-{}.html'.format(i) for i in range(1,51)]

def scrape_book(book_url):
    book_data = {} 
    page = requests.get(book_url, timeout=20)
    soup = BeautifulSoup(page.content,  "html.parser")
    
    
    with  open('un_produit.csv',mode='w', encoding='utf8', newline='') as file:
        fieldnames = ['title','price','Availability','UPC', 'Categories','Star','Src','Description','url']
        writer =  csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'title': 'A Light in the Attic', 'price':'£51.77','Availability':'In stock (22 available)', 'UPC':'a897fe39b1053632', 'Categories':'Poetry','Star':'star-rating Three',
                        'Src':'http://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg','url':'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'})
                         
        book_data['Title'] = soup.find("h1").text
        book_data['Price'] = soup.find("p",{"class":"price_color"}).get_text()
        book_data['Availability'] = soup.find("p", {"class":"instock availability"}).get_text().strip()
        book_data['UPC'] = soup.find("td").text
        book_data['Categories'] =  soup.find_all("li")[2].get_text().strip()
        book_data['rating'] = soup.find("p", class_="star-rating").get("class")[1]
        book_data['Img'] ="http://books.toscrape.com/"+ soup.find("img")['src'][6:].strip()
        book_data['url'] ='https://books.toscrape.com/index.html' + soup.find('a')['href'][12:]
        book_data['Product Description'] = soup.find_all("p")[3].text
        
            
    return book_data
print(scrape_book(url))