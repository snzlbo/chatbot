import csv
import re
from datetime import date
from ntpath import join
from misc.classTypes import Category
from misc.scrape import UseBeautifulSoup as useScrape
from misc.adScrape import advertisementScrape as useAdScrape
from misc.pagination import createLinkList as createLinkList

initialUrl = 'https://www.zangia.mn/'
today = str(date.today())
# all categories set
categorySet = set()
# all advertisement's link set
adUrlDict = {}
# all ads object set
adsSet = set()

# scrape initial links
soup = useScrape(initialUrl)
navigatorList = soup.find_all('div', class_='filter')
for navigator in navigatorList:
    if navigator.find('h3').text.strip() != 'Салбар, мэргэжил':
        continue
    # ALL CATEGORY LINKS
    categoryList = navigator.find_all('div')

for categoryItem in categoryList:
    categories = categoryItem.find('a')
    url = initialUrl + categories['href']
    tempCategory = Category(url, categories.text, '')
    print('CATEGORY LINK SCRAPED! ', url)
    soup = useScrape(url)
    subCategory = soup.find('div', class_='pros')
    # ALL SUBCATEGORY LINKS
    subCategoryList = subCategory.find_all('a')
    for subCategoryItem in subCategoryList:
        subCategoryUrl = initialUrl + subCategoryItem['href']
        tempSubCategory = Category(
            subCategoryUrl, subCategoryItem.text, tempCategory.name)
        categorySet.add(tempSubCategory)

for categoryItem in categorySet:
    if categoryItem.parentId == '':
        continue
    soup = useScrape(categoryItem.url)
    hasPagination = soup.find('div', class_='page-link')
    pagesUrl = []
    if hasPagination != None:
        pagesUrl = createLinkList(hasPagination, categoryItem.url)
    else:
        pagesUrl.append(categoryItem.url)
    for pageUrl in pagesUrl:
        soup = useScrape(pageUrl)
        ads = soup.find_all('div', class_='ad')
        # CREATE UNIQUE AD DICTIONARY
        for ad in ads:
            adUrl = initialUrl+ad.find('a', class_=None)['href']
            adUrlDict[adUrl] = categoryItem
    print(pagesUrl)
    pagesUrl.clear()

print(adUrlDict)
for adUrl in adUrlDict:
    tempAdItem = useAdScrape(adUrl)
    tempAdItem.setCategory(adUrlDict[adUrl])
    adsSet.add(tempAdItem)

file = open(today+'adScrape.csv', 'w', encoding='utf-8')
file.write('Parent Category Name' + '\t' +
           'Category Name ' + '\t' +
           'Link' + '\t' +
           'Employee Company' + '\t' +
           'Title' + '\t' +
           'Roles' + '\t' +
           'Requirements' + '\t' +
           'Additional Info' + '\t' +
           'Location' + '\t' +
           'Level' + '\t' +
           'Type' + '\t' +
           'Min Salary' + '\t' +
           'Max Salary' + '\t' +
           'Address' + '\t' +
           'Phone' + '\t' +
           'Fax' + '\t' +
           'Ad Added Date' + '\n')

for ad in adsSet:
    try:
        file.write(
            ad.category.parentId+'\t' +
            ad.category.name+'\t' +
            ad.url+'\t' +
            ad.company+'\t' +
            ad.title+'\t' +
            ad.roles+'\t' +
            ad.requirements+'\t' +
            ad.additionalInfo+'\t' +
            ad.location+'\t' +
            ad.level+'\t' +
            ad.type+'\t' +
            ad.minSalary+'\t' +
            ad.maxSalary+'\t' +
            ad.address+'\t' +
            ad.phoneNumber+'\t' +
            ad.fax+'\t' +
            ad.adAddedDate+'\n')
    except:
        print('File write error')

file.close()
