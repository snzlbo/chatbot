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
categoryList = navigatorList[2].find_all('div')

for categoryItem in categoryList:
    # all parent category link
    categories = categoryItem.find('a')
    url = 'https://www.zangia.mn/' + categories['href']
    tempCategory = Category(url, categories.text)
    categorySet.add(tempCategory)

    # all subcategory link
    soup = useScrape(url)
    subCategory = soup.find('div', class_='pros')
    subCategoryList = subCategory.find_all('a')
    for subCategoryItem in subCategoryList:
        url = 'https://www.zangia.mn/' + subCategoryItem['href']
        tempSubCategory = Category(
            url, subCategoryItem.text, tempCategory.name)
        categorySet.add(tempSubCategory)

for categoryItem in categorySet:
    # print('category:', categoryItem.parentId, 'subCategory:', categoryItem.name, 'url:', categoryItem.url)
    soup = useScrape(categoryItem.url)
    hasPagination = soup.find('div', class_='page-link')
    if hasPagination != None:
        pagesLink = createLinkList(hasPagination)
        for pageLink in pagesLink:
            soup = useScrape(pageLink)
            advertisementList = soup.find_all('div', class_='ad')
        print(advertisementList)
        break
    advertisementList = soup.find_all('div', class_='ad')
    print(advertisementList)
    # for ads in advertisementList:
    #   singleAdsItem = ads.find('a')
    #   url = 'https://www.zangia.mn/' + singleAdsItem['href']

    #   # ##extracting advertisement infos
    #   # tempAdItem = useAdScrape(url)
    #   # tempAdItem.setCategory(categoryItem)
    #   # adsSet.add(tempAdItem)

    #   soup = useScrape(url)
    #   ads = Advertisement(url, soup.find('h3').text.strip(), categoryItem)
    #   sectionList = soup.find_all('div', class_='section')
    #   for sectionItem in sectionList:
    #     subTitle = sectionItem.find('div', class_='details')
    #     print(subTitle)
    # break
