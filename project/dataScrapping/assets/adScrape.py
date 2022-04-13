import re
from .classTypes import Advertisement
from .scrape import UseBeautifulSoup as useScrape


def listScraper(sections, key) -> str:
    content = []
    for section in sections:
        subTitle = section.find('h2', class_=None).text
        if key != subTitle:
            continue
        div = section.find('div', class_=None)
        children = div.next_element

        while(children != None):
            try:
                content.append(textStrip(children.text))
                children = children.next_sibling
                continue
            except:
                print('An error occured')
            children = children.next_sibling
        content = [s for s in filter(listFunc, content)]
    if not content:
        return ''
    return ' '.join(content)


def textStrip(text) -> str:
    pattern = re.compile('[\r\n\xa0\t ]+', re.MULTILINE | re.IGNORECASE)
    return pattern.sub(' ', text.strip())


def listFunc(e):
    return len(e) != 0


def singleItemScraper(sections, key, subKey) -> str:
    for section in sections:
        subTitle = section.find('h2', class_=None).text
        if key != subTitle:
            continue
        div = section.find_all('div', class_=None)
        for item in div:
            if item.next_element.text == subKey:
                return textStrip(item.find('span').text)
    return 'None'


def salaryScraper(salary):
    print(salary)
    isDealable = ''
    k = re.split(r'[^\d,]+', salary, 2, re.IGNORECASE)
    if len(k) < 2:
        [a] = k[0]
        return a, a, isDealable
    if k[1] == '':
        a = k[0]
        return a, a, isDealable
    [a, b] = k[0:2]
    if len(k) > 2:
        isDealable = 'Тохиролцоно'
    return a, b, isDealable


def locationScrapper(location):
    city = ''
    district = ''
    k = location.split(',')
    if len(k) < 2:
        city = k[0]
        return city, district
    [city, district] = k[0:2]
    return city, district


def advertisementScrape(url) -> Advertisement:
    soup = useScrape(url)
    advertisement = Advertisement(url, soup.find('h3').text.strip())
    try:
        companyTitle = soup.find('div', class_='nlp').find('td')
        for item in companyTitle:
            if item.name == None:
                advertisement.company = textStrip(item.text)
    except:
        print('Company name scrape error')

    sections = soup.find_all('div', class_='section')
    # all items
    advertisement.level = singleItemScraper(sections, 'Бусад', 'Түвшин')
    advertisement.type = singleItemScraper(sections, 'Бусад', 'Төрөл')
    minSalary, maxSalary, isDealable = salaryScraper(
        singleItemScraper(sections, 'Бусад', 'Цалин'))
    advertisement.setSalary(minSalary, maxSalary, isDealable)
    city, district = locationScrapper(
        singleItemScraper(sections, 'Бусад', 'Байршил'))
    advertisement.location.city = city
    advertisement.location.district = district
    advertisement.location.exactAddress = singleItemScraper(
        sections, 'Холбоо барих', 'Хаяг')
    advertisement.roles = listScraper(
        sections, 'Гүйцэтгэх үндсэн үүрэг')
    advertisement.requirements = listScraper(
        sections, 'Ажлын байранд тавигдах шаардлага')
    advertisement.additionalInfo = listScraper(
        sections, 'Нэмэлт мэдээлэл')
    advertisement.contact.phoneNumber = singleItemScraper(
        sections, 'Холбоо барих', 'Утас')
    advertisement.contact.fax = singleItemScraper(
        sections, 'Холбоо барих', 'Факс')
    advertisement.adAddedDate = singleItemScraper(
        sections, 'Зарын хугацаа', 'Зар нийтлэсэн огноо')
    print('SINGLE AD SCRAPPING DONE!!!', url)

    return advertisement
