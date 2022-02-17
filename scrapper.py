from bs4 import BeautifulSoup
import requests

class Icategories:
  url = ''
  categoryName = ''
  parentId = ''
  def __init__(self, url, categoryName, parentId = None) -> None:
      self.url = url
      self.categoryName = categoryName
      self.parentId = parentId

class IcontactInfos:
  address = ''
  phoneNumber = ''
  fax = ''
  def __init__(self, address, phoneNumber, fax = None) -> None:
      self.address = address
      self.phoneNumber = phoneNumber
      self.fax = fax

class Iadvertiement:
  roles = ''
  requirements = ''
  location = ''
  level = ''
  type = ''
  salary = ''
  def __init__(self) -> None:
    pass

categorySet = set()
url = 'https://www.zangia.mn'

response = requests.get(url)  
soup = BeautifulSoup(response.text, 'html.parser')
navigatorList = soup.find_all('div', class_='filter')
categoryList = navigatorList[2].find_all('div')

for categoryItem in categoryList:
  categories = categoryItem.find('a')
  url = 'https://www.zangia.mn/' + categories['href']
  tempCategory = Icategories(url, categories.text)
  categorySet.add(tempCategory)
  
  response = requests.get(url)
  if response.status_code != 200:
   print(response.status_code)
   continue

  soup = BeautifulSoup(response.text, 'html.parser')
  subCategory = soup.find('div', class_='pros')
  subCategoryList = subCategory.find_all('a')
  for subCategoryItem in subCategoryList:
    url = 'https://wwww.zangia.mn/' + subCategoryItem['href']
    print(url)
    tempSubCategory = Icategories(url, subCategoryItem.text, tempCategory.categoryName)
    categorySet.add(tempSubCategory)

