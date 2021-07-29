import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler', params= {'tag_from': 'wp_cb_mostPopular_more'})

soup = BeautifulSoup(html_doc.text, 'html.parser')

popoler_area = soup.find(attrs={'class':'grid-row list-content'})
titles = popoler_area.findAll(attrs={'class':'media__title'})
images = popoler_area.findAll(attrs={'class':'media__image'})

for image in images:
    print (image.find('a').find('img')['title'])
# for index, title in enumerate (titles,1):
#     print (index, '.', title.text)
# print(titles)
