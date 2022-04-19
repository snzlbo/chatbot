from assets.classTypes import Advertisement, Category
from assets.scrape import UseBeautifulSoup as useScrape
from assets.adScrape import advertisementScrape as useAdScrape
from assets.spliter import createLinkList, splitUrl
from connection import Base, db, session
from insert import upsertAdvertisement, upsertCategory

initialUrl = 'https://www.zangia.mn/'
categorySet = set()
adUrlDict = {}


soup = useScrape(initialUrl)
navigatorList = soup.find_all('div', class_='filter')
for navigator in navigatorList:
    if navigator.find('h3').text.strip() != 'Салбар, мэргэжил':
        continue
    categoryList = navigator.find_all('div')

for categoryItem in categoryList:
    categories = categoryItem.find('a')
    url = initialUrl + categories['href']
    tempCategory = Category(splitUrl(url, 'b.'), url, categories.text)
    print('CATEGORY LINK SCRAPED! ', url, tempCategory.id)
    soup = useScrape(url)
    subCategory = soup.find('div', class_='pros')
    subCategoryList = subCategory.find_all('a')
    for subCategoryItem in subCategoryList:
        subCategoryUrl = initialUrl + subCategoryItem['href']
        tempSubCategory = Category(splitUrl(subCategoryUrl, 'r.'),
                                   subCategoryUrl, subCategoryItem.text, tempCategory)
        categorySet.add(tempSubCategory)
    categorySet.add(tempCategory)

for categoryItem in categorySet:
    if categoryItem.parentCategory == None:
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
        for ad in ads:
            adUrl = initialUrl+ad.find('a', class_=None)['href']
            adUrlDict[adUrl] = categoryItem
    print(pagesUrl)
    pagesUrl.clear()

for adUrl in adUrlDict:
    tempAdItem = useAdScrape(adUrl)
    tempAdItem.setCategory(adUrlDict[adUrl])
    tempAdItem.setId(splitUrl(adUrl, 'ad'))
    try:
        upsertAdvertisement(tempAdItem, tempAdItem.category)
    except:
        print('Write to db error')
    del tempAdItem
