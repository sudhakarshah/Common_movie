#Basic rating scrape to see how it works

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin # For joining next page url with base url

search_terms = "superman"

url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + '+'.join(search_terms) + '&s=all'

def next_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print (soup.prettify().encode('utf-8'))

    next_page = soup.find('td', 'result_text').find('a').get('href')

    return next_page


def movie_data(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, "html.parser")

    rating = soup.find('span', {'itemprop': 'ratingValue'}).get_text()

    return rating


next_page_url = next_page(url)

new_page = urljoin(url, next_page_url)

print(movie_data(new_page))
