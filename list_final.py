from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urljoin # For joining next page url with base url

director = "Anurag Kashyap"
producer = "Steven Spielberg"
actor = "Shah Rukh Khan"
director_li=[]
producer_li=[]
actor_li=[]
director_url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + '+'.join(director) + '&s=all'
producer_url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + '+'.join(producer) + '&s=all'
actor_url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + '+'.join(actor) + '&s=all'


def next_page(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, "html.parser")
    #print (soup.prettify().encode('utf-8'))

    next_page_url = soup.find('td', 'result_text').find('a').get('href')
    new_page = urljoin(url, next_page_url)
    return (new_page)


def movie_data(page_url,text):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, "html.parser")

    regular=re.compile(text)
    movie_li=[]
    movie_all_html = soup.findAll('div',{'id':regular})
    for movie in movie_all_html:
        movie_li.append(movie.find('a').get_text())
    return movie_li

director_page_url=next_page(director_url)
director_li=movie_data(director_page_url,"^director-t")
producer_page_url=next_page(producer_url)
producer_li=movie_data(producer_page_url,"^producer-t")
actor_page_url=next_page(actor_url)
actor_li=movie_data(actor_page_url,"^actor-t")

print (director_li)
print (producer_li)
print (actor_li)
