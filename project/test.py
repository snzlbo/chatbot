import time
from assets.classTypes import Category
from assets.scrape import UseBeautifulSoup as useScrape
from assets.adScrape import advertisementScrape as useAdScrape
from assets.pagination import createLinkList as createLinkList

start_time = time.time()
url = 'https://www.zangia.mn/job/_fwpwba+kld'

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

cate = Category(url, 'Бусад', 'Банк, санхүү, нягтлан бодох бүртгэл')
try:
    tempAdItem = useAdScrape(url)
    tempAdItem.setCategory(cate)
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


except:
    print('Ad writing error')
file.close()
print("--- %s seconds ---" % (time.time() - start_time))
