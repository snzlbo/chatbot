from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError

def UseBeautifulSoup(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
  except HTTPError as error:
    print(error)
  soup = BeautifulSoup(response.text, 'html.parser')
  return soup