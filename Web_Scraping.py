#COINBASE SCRAPER

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
#
#
# class CoinbaseScraper:
#     def __init__(self, url):
#         self.url = url
#         self.soup = None
#
#     def fetch(self):
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
#         response = requests.get(self.url, headers=headers)
#         if response.status_code == 200:
#             self.soup = BeautifulSoup(response.text, 'html.parser')
#         else:
#             print("Error fetching..")
#
#     def parse(self):
#         table_data = []
#         table = self.soup.find('table')
#         rows = table.find_all('tr')
#         for row in rows:
#             columns = row.find_all('td')
#             row_data = [col.text.strip() for col in columns]
#             if row_data:
#                 table_data.append(row_data)
#         if table_data:
#             df = pd.DataFrame(table_data[1:],
#                               columns=['Name', 'Price', 'chart', 'Market Cap', 'Change', 'Close', 'Supply', 'Trade'])
#             print(df)
#         else:
#             print("No data")
#
#     def run(self):
#         self.fetch()
#         if self.soup:
#             self.parse()
#
#
# scraper = CoinbaseScraper('https://www.coinbase.com/explore')
# scraper.run()

#VARLE.LT SCRAPER

# import requests
# from bs4 import BeautifulSoup

# class VarleScraper:
#     def __init__(self, url):
#         self.url = url
#         self.soup = None
#
#     def fetch(self):
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
#         response = requests.get(self.url, headers=headers)
#         if response.status_code == 200:
#             self.soup = BeautifulSoup(response.text, 'html.parser')
#         else:
#             print("Something went wrong..")
#
#     def parse_page(self):
#         product_list = []
#         products = self.soup.find_all('div', class_='GRID_ITEM')
#         for product in products:
#             product_name = product.find('div', class_='product-title').text.strip()
#             product_price = product.find('span', class_='price-value').text.strip().replace('\n\xa0, '')
#             rating = product.find('li', attrs={'class': 'rating'}).text.strip().replace('\n' '')[:3]
#             # print(product_price)
#             product_list.append({
#                 'Produkto pavadinimas': product_name,
#                 'Produkto kaina': product_price,
#                 'Ivertinimas': rating
#             })
#         print(product_list)
#
#     def run(self):
#         self.fetch()
#         if self.soup:
#             self.parse_page()
#
# scraper = VarleScraper('https://www.varle.lt/isoriniai-kietieji-diskai-hdd/')
# scraper.run()

# def fetch_page(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.text
#     else:
#         return None
#
# def parse_page(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     product_list = []
#     products = soup.find_all('div', {'GRID_ITEM'})
#     for product in products:
#         product_name = product.find('div', class_='product-title').text.strip()
#         product_price = product.find('span', class_='price-value').text.strip()
#
#         product_list.append({
#             'Produkto pavadinimas': product_name,
#             'Produkto kaina': product_price
#         })
#     return product_list
#
# def scrape_page(base_url, start_page=1, max_page=5):
#     #https://www.varle.lt/isoriniai-kietieji-diskai-hdd/?p=3
#     all_products = []
#     current_page = start_page
#     while current_page <= max_page:
#         url = f"{base_url}?p={current_page}"
#         print(f"Scraping page {url}")
#         html = fetch_page(url)
#         if html:
#             has_products = parse_page(html)
#             if has_products:
#                 all_products.extend(has_products)
#                 print(all_products)
#             else:
#                 print("No more products found! Stopping...")
#                 break
#         else:
#             print("Failed to retrieve page!")
#             break
#         current_page += 1
#     print(f"Total products: {len(all_products)}")
#     for product in all_products:
#         print(product)
#
# base_url = "https://www.varle.lt/isoriniai-kietieji-diskai-hdd/"
# scrape_page(base_url)

#SPAIN REAL ESTATE SCRAPING

# import requests
# from bs4 import BeautifulSoup
#
#
# def fetch_page(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.text
#     else:
#         return None
# def parse_page(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     object_list = []
#     objects = soup.find_all('li', {'data-object': True})
#
#     for object in objects:
#         object_name = object.find('div', class_='title').text.strip()
#         object_price = object.find('div', class_='price js-list-for-show')
#         object_bedroom = object.find('span', class_='bedrooms')
#         object_bathroom = object.find('span', class_='bathrooms')
#         object_area = object.find('span', class_='area')
#
#         if object_price:
#             object_price = object_price.text.strip
#         else:
#             print('Informacijos nera')
#         if object_bedroom:
#             object_bedroom = object_bedroom.text.strip
#         else:
#             print('Informacijos nera')
#         if object_area:
#             object_area = object_area.text.strip
#         else:
#             print('Informacijos nera')
#
#
#
#         object_list.append({
#             'Objekto pavadinimas': object_name,
#             'Objekto kaina': object_price,
#             'Objekto miegamieji kambariai': object_bedroom,
#             'Objekto vonios kambariai': object_bathroom,
#             'Objekto areas': object_area
#              })
#
#     return object_list
#
# def scrape_page(base_url, start_page=1, max_page=18):
#     all_objects = []
#     current_page = start_page
#     while current_page <= max_page:
#         url = f"{base_url}page/{current_page}"
#         print(f"Scraping page {url}")
#         html = fetch_page(url)
#         if html:
#             has_objects = parse_page(html)
#             if has_objects:
#                 all_objects.extend(has_objects)
#                 print(all_objects)
#             else:
#                 print("No more products found! Stopping...")
#                 break
#         else:
#             print("Failed to retrieve page!")
#             break
#         current_page += 1
#     print(f"Total products: {len(all_objects)}")
#     for object in all_objects:
#         print(object)
#
# base_url = "https://spain-real.estate/property/andalusia/sevilla/page/1/#objects"
# scrape_page(base_url)


# FIFAFINDER SCRAPING
#
#
# import requests
# from bs4 import BeautifulSoup
# import os
#
# def parsisiusti_puslapi(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         print(f"Puslapis pasiekimas: {url}")
#         return response.text
#     else:
#         print(f"Nepavyko pasiekti puslapio. Svetainė grąžino {response.status_code}.")
#         return None
#
# def istraukti_zaideju_info(html):
#     zaideju_info = []
#     soup = BeautifulSoup(html, 'html.parser')
#     zaidejai = soup.find_all('tr',  attrs={'data-playerid': True})
#     for zaidejas in zaidejai:
#         vardas = zaidejas.find('td', attrs={'data-title': "Name"}).text.strip()
#         # print(vardas)
#
#         age = int(zaidejas.find('td', attrs={'data-title': "Age"}).text.strip())
#
#         team1 = zaidejas.find('td', attrs={'data-title': "Team"})
#         team = team1.find('img').get('alt').strip().replace(' FIFA 24','')
#
#         nationality1 = zaidejas.find('td', attrs={'data-title': "Nationality"})
#         nationality = nationality1.find('img').get('alt').strip().replace(' FIFA 24', '')
#
#         # OVR_POT = zaidejas.find_all('span', attrs={'class': 'badge badge-dark rating'}) # kažkodėl grąžina tuščią
#         OVR_POT = zaidejas.find_all('span', class_='rating')
#         # print(OVR_POT)
#         OVR = int(OVR_POT[0].text.strip())
#         POT = int(OVR_POT[1].text.strip())
#
#         positions1 = zaidejas.find('td', attrs={'data-title': "Preferred Positions"})
#         positions2 = positions1.find_all('span', class_='position')
#         positions = [poz.text.strip() for poz in positions2]
#         # positions = ', '.join(positions)
#
#         zaidejo_info = {
#             'Name': vardas,
#             'Age': age,
#             'Team': team,
#             'Nationality': nationality,
#             'OVR': OVR,
#             'POT': POT,
#             'Positions': positions
#         }
#         # print(zaidejo_info)
#         zaideju_info.append(zaidejo_info)
#     return zaideju_info
#
#
# def nuskaityti_vietini_puslapi(html_rinkmena):
#     turinys = ''
#     with open(html_rinkmena, mode='r', encoding='utf-8') as rinkmena:
#         turinys_eilutese = rinkmena.readlines()
#         for eilute in turinys_eilutese:
#             turinys += eilute
#     return turinys
#
# def irasyti_kaip_vietini(turinys, html_rinkmena):
#     with open(html_rinkmena, mode='w', encoding='utf-8') as rinkmena:
#         rinkmena.writelines(turinys)
#
# def main():
#     url = 'https://www.fifaindex.com/'
#     html_rinkmena = 'FIFA_index.html'
#
#     if os.path.exists(html_rinkmena):
#         print("Bandoma įkelti iš vietinio HTML:", html_rinkmena)
#         html = nuskaityti_vietini_puslapi(html_rinkmena)
#     else:
#         print("Bandoma pasiekti internetinį puslapį", url)
#         html = parsisiusti_puslapi(url)
#         # įrašyti pakartotiniam naudojimui, kad nebereiktų siųstis iš interneto
#         irasyti_kaip_vietini(html, html_rinkmena)
#
#     if html:
#         print("Pavyko gauti HTML turinį.")
#         zaideju_info = istraukti_zaideju_info(html)
#         print("Gauti žaidėjai:", len(zaideju_info))
#         # print(zaideju_info)
#         for zaidejo_info in zaideju_info:
#             print(zaidejo_info)
#     else:
#         print("Negalime pateikti filmų informacijos.")
#
# main()

#IMBD SCRAPING
from time import sleep
import requests
from bs4 import BeautifulSoup


def get_soup(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def get_movie_urls(base_url, top_movie_url, headers):
    soup = get_soup(top_movie_url, headers)
    movie_links = soup.find_all('li', class_='ipc-metadata-list-summary-item')
    movie_urls = [base_url + movie.find('a')['href'] for movie in movie_links]
    return movie_urls


def get_movie_data(movie_url, headers):
    soup = get_soup(movie_url, headers)
    title = soup.find('h1').text.strip()
    genre = soup.find('span', class_='ipc-chip__text').text.strip()

    return {'url': movie_url, 'title': title, 'genre': genre}


def main():
    base_url = 'https://www.imdb.com/'
    top_movies_url = 'https://www.imdb.com/chart/top/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/58.0.3029.110 Safari/537.3'}
    movie_urls = get_movie_urls(base_url, top_movies_url, headers)
    for url in movie_urls[:5]:
        details = get_movie_data(url, headers)
        print(details)
        sleep(1)


if __name__ == '__main__':
    main()


