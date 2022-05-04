import bs4
import requests
from os import system
system('cls||clear')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

def post_full_text (post_url):
    post_req = requests.get(post_url,headers=headers)
    post_req.raise_for_status()
    post_soap = bs4.BeautifulSoup(post_req.text,features='html.parser')
    post_full_text = post_soap.find('div',class_='tm-article-body')
    return post_full_text.text

url = 'https://habr.com/ru/all/'

req = requests.get(url,headers=headers)
req.raise_for_status()
text = req.text

soap = bs4.BeautifulSoup(text,features='html.parser')
articles = soap.find_all('article')
for article in articles:
    post_header = article.find('h2',class_='tm-article-snippet__title tm-article-snippet__title_h2').text
    post_date = (article.find('time').get('title')).split(',')[0].split('-')
    post_date = f'{post_date[2]}.{post_date[1]}.{post_date[0]}'
    post_priview = article.find('div',class_='tm-article-body tm-article-snippet__lead').text
    post_link = url[0:16] + article.find('a',class_='tm-article-snippet__title-link').get('href')
    post_full = post_full_text(post_link)
    for search_word in KEYWORDS:
        if (search_word.lower() in post_header.lower()) or (search_word.lower() in post_priview.lower()) or (search_word.lower() in post_full.lower()):
            print (f'{post_date} - {post_header} - {post_link} [найдено слово - {search_word.lower()}]')
   
