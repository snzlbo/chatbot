from bs4 import BeautifulSoup
import requests

categories_set = set()

url = 'https://www.zangia.mn'
response = requests.get(url)
if response.status_code != 200:
  print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
category_list = soup.find_all('div', class_='filter')
categories = category_list[2].find_all('div')

for item in categories:
  a = item.find('a')
  categories_set.add('https://www.zangia.mn/'+a['href'])
print(categories_set)

