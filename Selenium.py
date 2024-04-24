# --Importuojame reikalingas bibliotekas--
# --Importing necessary libraries--

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager  # ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# --Apibreziame svetaines URL taikini--
# --Defining the target URL for scraping--

target = ['https://ibiblioteka.lt/metis/publication?q=yubs6a4wr']

# --Aprasome funkcija, kuri naudoja URL sąrašą kaip įvestį ir pateikia žodynų sąrašą,
#      kuriame yra nukopijuoti knygos duomenys--
# --Defining a function that takes a list of URLs as input and returns a list of dictionaries
#       containing the scrapped book data--
def scrape_books_data(urls):
    books_data = []   #--Sukuriame sarasa--creating a list--
    #--Idiegiame ir valdome Firefox WebDriver--
    #--Installing and managing the Firefox WebDriver--
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    for index, url in enumerate(urls):
        driver.get(url)
        time.sleep(12)

        #--Komanduojame spusteleti elementus, laukiame, kol elementus bus galima
        #     spusteleti, ir spausdiname pranesimus i konsole--
        #--We command to click on elements, waiting for elements to be clickable,
        #     and printing messages to the console--
        if index == 0:
            try:
                open_dropdown = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'mat-form-field.ng-tns-c69-2')))
                open_dropdown.click()
                time.sleep(2)
                print('Isskleidziamas meniu paspaustas')
                third_option = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '#mat-option-2')))  #
                third_option.click()
                time.sleep(2)
                print('Pasirinktas 3 meniu elementas')
                search_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.c-btn--cta'))
                )
                search_button.click()
                time.sleep(3)
                print("Paieskos mygtukas paspaustas")

                cookie_agreement = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'app-button.cookie-agreement__button:nth-child(1)'))
                )
                cookie_agreement.click()
                print('Accepted Cookie agreement!')

                #--Sis kodo blokas bando keturis kartus spusteleti mygtuka „Ikelti daugiau“.
                # Jei mygtukas nerastas arba spustelejus mygtuka ivyko klaida,
                # kodas isspausdina klaidos pranesima ir iseina is ciklo--

                #--This code block attempts to click on the "Load more" button four times.
                # If the button is not found or if an error occurs while clicking the button,
                # the code prints an error message and breaks out of the loop--
                for _ in range(4):
                    try:
                        load_more = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, '.mat-stroked-button'))
                        )
                        load_more.click()
                        print('Daugiau rezultatu mygtukas paspaustas')
                        time.sleep(3)
                    except (NoSuchElementException, TimeoutException, ElementClickInterceptedException) as e:
                        print(f'Error while clicking "Load more": {e}')
                        break

                    #--Naudojame Beautiful Soup pasisavinti tinklalapio turini--
                    #--We use Beautiful Soup to scrap website content--
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    table = soup.find('table', class_='c-data-table')
                    if table:
                        for row in table.find_all('tr')[1:]:
                            cells = row.find_all('td')
                            if cells:
                                title_data = cells[1].text.split("Pavadinimas:")[-1]
                                books_data.append({
                                    'title': title_data
                                })
                    else:
                        print('No table found')
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    table = soup.find('table', class_='c-data-table')
                    if table:
                        for row in table.find_all('tr')[1:]:
                            cells = row.find_all('td')
                            if cells:
                                title_data = cells[1].text.split("Pavadinimas:")[-1]
                                books_data.append({
                                    'title': title_data
                                })
                    else:
                        print('No table found')

            except Exception as e:
                print(f"Error Occurred {e}")

##--Sis kodo blokas uzdaro narsykle ir grazina knygu duomenu sarasa.
#--This code block quits the web driver and returns the list of books data.
    driver.quit()
    return books_data


all_data = []

for url in target:
    data = scrape_books_data(target)
    all_data.extend(data)


print(all_data)
