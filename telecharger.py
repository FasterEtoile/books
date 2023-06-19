import requests
from bs4 import BeautifulSoup
import os

# Créer un dossier pour stocker les images
if not os.path.exists('images'):
    os.makedirs('images')

url = 'https://books.toscrape.com/'

# Liste des URLs des pages à visiter
urls = [url]
for i in range(1, 51):
    urls.append(f'{url}catalogue/page-{i}.html')

# Parcourir toutes les pages et extraire les liens des images
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')

    # Télécharger chaque image
    for img in images:
        img_url = img['src'].replace('../', '')
        img_name = img_url.split('/')[-1]
        img_path = f'images/{img_name}'
        img_response = requests.get(f'https://books.toscrape.com/{img_url}')
        with open(img_path, 'wb') as f:
            f.write(img_response.content)




