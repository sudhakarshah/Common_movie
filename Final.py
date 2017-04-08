from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urljoin # For joining next page url with base url
 # A dot means the user does not want to search that criteria
director = "."
producer = "Karan Johar"
actor = "Shah Rukh Khan"
actress = "Kajol"
director_li=[]
producer_li=[]
actor_li=[]
actress_l1=[]
director_url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + '+'.join(director) + '&s=all'
producer_url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + '+'.join(producer) + '&s=all'
actor_url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + '+'.join(actor) + '&s=all'
actress_url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + '+'.join(actress) + '&s=all'

user_inp_count=4
if(director=='.'):
    user_inp_count=user_inp_count-1
if(producer=='.'):
    user_inp_count=user_inp_count-1
if(actor=='.'):
    user_inp_count=user_inp_count-1
if(actress=='.'):
    user_inp_count=user_inp_count-1

def next_page(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, "html.parser")
    #print (soup.prettify().encode('utf-8'))

    next_page_url = soup.find('td', 'result_text').find('a').get('href')
    new_page = urljoin(url, next_page_url)
    return (new_page)


def movie_data(next_page_url,text):
    response = requests.get(next_page_url)
    soup = BeautifulSoup(response.text, "html.parser")

    regular=re.compile(text)
    movie_li=[]
    movie_all_html = soup.findAll('div',{'id':regular})
    for movie_soup in movie_all_html:
        # to ensure there is no repitition for the same person
        if movie_soup.find('a').get_text() not in movie_li:
            movie_li.append(movie_soup.find('a').get_text())
    return movie_li


director_page_url=next_page(director_url)
director_li=movie_data(director_page_url,"^director-t*")
producer_page_url=next_page(producer_url)
producer_li=movie_data(producer_page_url,"^producer-t*")
actor_page_url=next_page(actor_url)
actor_li=movie_data(actor_page_url,"^actor-t*")
actress_page_url=next_page(actress_url)
actress_li=movie_data(actress_page_url,"^actress-t*")

#print (director_li)
#print (producer_li)
#print (actor_li)
#print (actress_li)

movie_dict={}

def check(movie_name):
    if movie_name in movie_dict:
        movie_dict[movie_name]=movie_dict[movie_name]+1

    else:
        movie_dict[movie_name]=1


for movie in director_li:
    check(movie)
for movie in actor_li:
    check(movie)
for movie in actress_li:
    check(movie)
for movie in producer_li:
    check(movie)




all_movie_name=movie_dict.keys()
for movie in all_movie_name:
    if movie_dict[movie]==user_inp_count:
        print(movie)




