from datetime import date
import time
from assets.classTypes import Category
from assets.scrape import UseBeautifulSoup as useScrape
from assets.adScrape import advertisementScrape as useAdScrape
from assets.pagination import createLinkList as createLinkList

start_time = time.time()
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
           'Is Dealable' + '\t' +
           'Address' + '\t' +
           'Phone' + '\t' +
           'Fax' + '\t' +
           'Ad Added Date' + '\n')
print(adUrlDict)
for adUrl in adUrlDict:
    print(adUrl)
    try:
        tempAdItem = useAdScrape(adUrl)
        tempAdItem.setCategory(adUrlDict[adUrl])
        file.write(
            tempAdItem.category.parentId+'\t' +
            tempAdItem.category.name+'\t' +
            tempAdItem.url+'\t' +
            tempAdItem.company+'\t' +
            tempAdItem.title+'\t' +
            tempAdItem.roles+'\t' +
            tempAdItem.requirements+'\t' +
            tempAdItem.additionalInfo+'\t' +
            tempAdItem.location+'\t' +
            tempAdItem.level+'\t' +
            tempAdItem.type+'\t' +
            tempAdItem.minSalary+'\t' +
            tempAdItem.maxSalary+'\t' +
            tempAdItem.isDealable+'\t' +
            tempAdItem.address+'\t' +
            tempAdItem.phoneNumber+'\t' +
            tempAdItem.fax+'\t' +
            tempAdItem.adAddedDate+'\n')
        del tempAdItem
    except:
        print('Ad writing error')
file.close()
print("--- %s seconds ---" % (time.time() - start_time))
