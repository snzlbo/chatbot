import time

from numpy import insert
from assets.classTypes import Category, Contact
from assets.scrape import UseBeautifulSoup as useScrape
from assets.adScrape import advertisementScrape as useAdScrape
from assets.spliter import createLinkList, splitUrl
from insert import PAdvertisement, PCategory, insertToAdvertisement
from connection import session

start_time = time.time()
# url = 'https://www.zangia.mn/job/_y1rqsntzr0'
# soup = useScrape(url)
# categorySet = set()
adUrlDict = {}

# # parent category scrape
# subCategory = soup.find('div', class_='pros')
# subCategoryList = subCategory.find_all('a')
# for subCategoryItem in subCategoryList:
#     subCategoryUrl = 'https://www.zangia.mn/' + subCategoryItem['href']
#     tempSubCategory = Category(
#         subCategoryUrl, subCategoryItem.text, 'Уул уурхай')
#     categorySet.add(tempSubCategory)

# for categoryItem in categorySet:
#     if(categoryItem.parentId == ''):
#         continue
#     soup = useScrape('https://www.zangia.mn/job/list/b.22/r.532')
#     hasPagination = soup.find('div', class_='paage-link')
#     pagesUrl = []
#     if hasPagination != None:
#         pagesUrl = createLinkList(hasPagination, categoryItem.url)
#     else:
#         pagesUrl.append(categoryItem.url)
#     for pageUrl in pagesUrl:
#         soup = useScrape(pageUrl)
#         ads = soup.find_all('div', class_='ad')
#         # CREATE UNIQUE AD DICTIONARY
#         for ad in ads:
#             adUrl = 'https://www.zangia.mn/'+ad.find('a', class_=None)['href']
#             adUrlDict[adUrl] = categoryItem
#     print(pagesUrl)
#     pagesUrl.clear()


# ## subcategoryScrape
# ca = Category('https://www.zangia.mn/job/list/b.36', 'Захиргаа, Хүний нөөц')
# cate = Category('https://www.zangia.mn/job/list/b.36',
#                 'Гадаад харилцаа', ca)
# soup = useScrape('https://www.zangia.mn/job/list/b.36/r.1334')
# hasPagination = soup.find('div', class_='page-link')
# pagesUrl = []
# if hasPagination != None:
#     pagesUrl = createLinkList(
#         hasPagination, 'https://www.zangia.mn/job/list/b.36/r.1334')
# else:
#     pagesUrl.append('https://www.zangia.mn/job/list/b.36/r.1334')
# for pageUrl in pagesUrl:
#     soup = useScrape(pageUrl)
#     ads = soup.find_all('div', class_='ad')
#     # CREATE UNIQUE AD DICTIONARY
#     for ad in ads:
#         adUrl = 'https://www.zangia.mn/'+ad.find('a', class_=None)['href']
#         adUrlDict[adUrl] = cate
# print(pagesUrl)
# pagesUrl.clear()

# file = open('test.csv', 'w', encoding='utf-8')
# file.write('Parent Category Name' + '\t' +
#            'Category Name ' + '\t' +
#            'Link' + '\t' +
#            'Employee Company' + '\t' +
#            'Title' + '\t' +
#            'Level' + '\t' +
#            'Type' + '\t' +
#            'Min Salary' + '\t' +
#            'Max Salary' + '\t' +
#            'Is Dealable' + '\t' +
#            'City/Province' + '\t' +
#            'District' + '\t'
#            'Exact Address' + '\t' +
#            'Roles' + '\t' +
#            'Requirements' + '\t' +
#            'Additional Info' + '\t' +
#            'Phone' + '\t' +
#            'Fax' + '\t' +
#            'Ad Added Date' + '\n')

# for adUrl in adUrlDict:
#     tempAdItem = useAdScrape(adUrl)
#     tempAdItem.setCategory(adUrlDict[adUrl])
#     print(tempAdItem.category.parentCategory.name)
#     file.write(
#         tempAdItem.category.parentCategory.name+'\t' +
#         tempAdItem.category.name+'\t' +
#         tempAdItem.url+'\t' +
#         tempAdItem.company+'\t' +
#         tempAdItem.title+'\t' +
#         tempAdItem.level+'\t' +
#         tempAdItem.type+'\t' +
#         tempAdItem.minSalary+'\t' +
#         tempAdItem.maxSalary+'\t' +
#         tempAdItem.isDealable+'\t' +
#         tempAdItem.location.city+'\t' +
#         tempAdItem.location.district+'\t' +
#         tempAdItem.location.exactAddress+'\t' +
#         tempAdItem.roles+'\t' +
#         tempAdItem.requirements+'\t' +
#         tempAdItem.additionalInfo+'\t' +
#         tempAdItem.contact.phoneNumber+'\t' +
#         tempAdItem.contact.fax+'\t' +
#         tempAdItem.adAddedDate+'\n')
#     del tempAdItem
# file.close()
# print("--- %s seconds ---" % (time.time() - start_time))

parentCate = Category(
    'b.19', 'https://www.zangia.mn/job/list/b.19', 'Аялал жуулчлал, зочид буудал')
cate = Category('r.486', 'https://www.zangia.mn/job/list/b.19/r.486',
                'Аялал жуулчлалын менежмент', parentCate)
contact = Contact('75055005', 'a')
adUrl = 'https://www.zangia.mn/job/_cbewxy0m2b'
test = useAdScrape(adUrl)
test.setCategory(cate)
test.setContact(contact)
test.setId(splitUrl(adUrl, 'ad'))

dict = PAdvertisement(test).__dict__
del dict['_sa_instance_state']
row = session.query(PAdvertisement).filter(PAdvertisement._id == test.id)
if row.first() == None:
    insertToAdvertisement(test)
else:
    row.update(dict, synchronize_session=False)
session.commit()
