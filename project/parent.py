from dataScrapping.assets.classTypes import Category
from dataScrapping.assets.scrape import UseBeautifulSoup as useScrape
from dataScrapping.assets.adScrape import advertisementScrape as useAdScrape
from dataScrapping.assets.pagination import createLinkList as createLinkList

# start_time = time.time()
initialUrl = 'https://www.zangia.mn/'
# today = str(date.today())
# all categories set
categorySet = set()
# all advertisement's link set
adUrlDict = {}
# all ads object set
adsSet = set()


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
    tempCategory = Category(url, categories.text)
    print('CATEGORY LINK SCRAPED! ', url)
    soup = useScrape(url)
    subCategory = soup.find('div', class_='pros')
    # ALL SUBCATEGORY LINKS
    subCategoryList = subCategory.find_all('a')
    for subCategoryItem in subCategoryList:
        subCategoryUrl = initialUrl + subCategoryItem['href']
        tempSubCategory = Category(
            subCategoryUrl, subCategoryItem.text, tempCategory)
        categorySet.add(tempSubCategory)
    categorySet.add(tempCategory)
    break

for categoryItem in categorySet:
    if categoryItem.parentId == None:
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


for adUrl in adUrlDict:
    print(adUrl, adUrlDict[adUrl])
