from misc.classTypes import Category
from misc.scrape import UseBeautifulSoup as useScrape
from misc.adScrape import advertisementScrape as useAdScrape
from misc.pagination import createLinkList as createLinkList

# all categories set
categorySet = set()
# all advertisement's link set
adUrlSet = set()
# all ads set
adsSet = set()
url = 'https://www.zangia.mn'

# scrape initial links
soup = useScrape(url)
navigatorList = soup.find_all('div', class_='filter')
categoryList = navigatorList[1].find_all('div')

for categoryItem in categoryList:
    # all parent category link
    categories = categoryItem.find('a')
    url = 'https://www.zangia.mn/' + categories['href']
    tempCategory = Category(url, categories.string)
    categorySet.add(tempCategory)

    # all subcategory link
    soup = useScrape(url)
    subCategory = soup.find('div', class_='pros')
    subCategoryList = subCategory.find_all('a')
    for subCategoryItem in subCategoryList:
        url = 'https://www.zangia.mn/' + subCategoryItem['href']
        tempSubCategory = Category(
            url, subCategoryItem.string, tempCategory.name)
        categorySet.add(tempSubCategory)

for categoryItem in categorySet:
    # print('category:', categoryItem.parentId, 'subCategory:', categoryItem.name, 'url:', categoryItem.url)
    if categoryItem.parentId == None:
        continue
    soup = useScrape(categoryItem.url)
    hasPagination = soup.find('div', class_='page-link')
    pagesUrl = []
    if hasPagination != None:
        pagesUrl = createLinkList(hasPagination, categoryItem.url)
    else:
        pagesUrl.append(categoryItem.url)
    print(pagesUrl)
    for adUrl in pagesUrl:
        print(adUrl)
        soup = useScrape(adUrl)
        ads = soup.find_all('div', class_='ad')
        for ad in ads:
            tempAdItem = useAdScrape(
                'https://www.zangia.mn/' + ad.find('a', class_=None)['href'])
            adsSet.add(tempAdItem.setCategory(categoryItem))
    pagesUrl.clear()
    break
