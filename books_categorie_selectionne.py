import csv
import requests
from bs4 import BeautifulSoup

# Définition de l'URL de la catégorie de livres à extraire
url = 'https://books.toscrape.com/catalogue/category/books/poetry_23/index.html'

# Envoyer une requête GET pour récupérer la page HTML
response = requests.get(url)
response.raise_for_status()

# Création de l'objet BeautifulSoup pour analyser le HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver tous les livres de la catégorie
books = soup.find_all('article', class_='product_pod')

# Création d'une liste pour stocker les données des livres
book_data = []

# Parcourir les livres et extraire les informations nécessaires
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='availability').text.strip()
    book_data.append([title, price, availability])

# Enregistrer les données dans un fichier CSV
csv_filename = 'livres.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Titre', 'Prix', 'Disponibilité'])
    writer.writerows(book_data)

print(f"Les données ont été extraites et enregistrées dans le fichier {csv_filename}.")
