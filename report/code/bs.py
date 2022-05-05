from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError

url = 'https://zangia.mn/'
try:
    response = requests.get(url)
    response.raise_for_status()
except HTTPError as error:
    print(error)
soup = BeautifulSoup(response.text, 'html.parser')
navigatorList = soup.find_all('div', class_='filter')
print(navigatorList[0])
