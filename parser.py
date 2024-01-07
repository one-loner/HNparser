from bs4 import BeautifulSoup
from random import randrange
import requests
import time

def parse_html(url,keyword):
    # Отправляем GET-запрос к странице
    response = requests.get(url)
    
    # Проверяем успешность запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Находим все теги 'a' (ссылки)
        links = soup.find_all('a')
        
        # Выводим на экран ссылки и их подписи
        for link in links:
            href = link.get('href')
            text = link.text.strip()
            if href and href.startswith('http'):
                if text != "API":
                   if text != "Legal":
                      if text != "Apply to YC":
                         if keyword.lower() in text.lower() or keyword.lower() in href.lower():
                            print(f"{text}\n{href}\n")
                         #if keyword.lower() in href.lower():
                            #print(f"{text}\n{href}\n")
    else:
        #print(f"Error code {response.status_code}")
        time.sleep(randrange(7)+1)
        parse_html(url,keyword) 

print("Welcome to HN parser. Enter search request or press Enter to pars all site.")
kw=input("> ")
if kw == '':
   kw = ' '

parse_html('https://news.ycombinator.com', kw)
for i in range(2, 17):
    print(i)
    parse_html('https://news.ycombinator.com/?p='+str(i), kw)
    time.sleep(randrange(7)+1)

