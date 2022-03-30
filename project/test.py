import time
from assets.classTypes import Category
from assets.scrape import UseBeautifulSoup as useScrape
from assets.adScrape import advertisementScrape as useAdScrape
from assets.pagination import createLinkList as createLinkList

start_time = time.time()
url = 'https://www.zangia.mn/job/list/b.15'
soup = useScrape(url)
categorySet = set()
adUrlDict = {}

subCategory = soup.find('div', class_='pros')
subCategoryList = subCategory.find_all('a')
for subCategoryItem in subCategoryList:
    subCategoryUrl = 'https://www.zangia.mn/' + subCategoryItem['href']
    tempSubCategory = Category(
        subCategoryUrl, subCategoryItem.text, 'Уул уурхай')
    categorySet.add(tempSubCategory)

for categoryItem in categorySet:
    if(categoryItem.parentId == ''):
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
            adUrl = 'https://www.zangia.mn/'+ad.find('a', class_=None)['href']
            adUrlDict[adUrl] = categoryItem
    print(pagesUrl)
    pagesUrl.clear()


file = open('test.csv', 'w', encoding='utf-8')
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

for adUrl in adUrlDict:
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
