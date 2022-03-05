from bs4 import BeautifulSoup
import requests


url = 'https://www.gourmetsleuth.com/features/wine-cheese-pairing-guide'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('td', attrs={"class": "pairings"})

# results = soup.find_all('div')

print(results)


def scraper(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    pairs = soup.find_all(
        'div', attrs={"class": "basiccontent basiccontent__icon"})
    urls = soup.find_all('a', attrs={"class": "link__default"})
    for company in companies:
        company_list.append(company.h3.text)

    urls = soup.find_all('a', attrs={"class": "link__default"})
    for url in urls:
        url_list.append(url.get('href'))
