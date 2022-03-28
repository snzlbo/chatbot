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
    isDealable = ''
    k = re.split(r'[^\d,]+', salary, 2, re.IGNORECASE)
    if len(k) < 2:
        [a] = k[0:1]
        return a, a
    [a, b] = k[0:2]
    if len(k) > 2:
        isDealable = 'Тохиролцоно'
    return a, b, isDealable


def advertisementScrape(url) -> Advertisement:
    soup = useScrape(url)
    advertisement = Advertisement(url, soup.find('h3').text.strip())
    companyTitle = soup.find('div', class_='nlp').find('td')
    for item in companyTitle:
        try:
            if item.name == None:
                advertisement.company = textStrip(item.text)
        except:
            print('Company name scrape error')
    # advertisement.company = textStrip(company)

    # all items
    sections = soup.find_all('div', class_='section')
    advertisement.roles = listScraper(
        sections, 'Гүйцэтгэх үндсэн үүрэг')
    advertisement.requirements = listScraper(
        sections, 'Ажлын байранд тавигдах шаардлага')
    advertisement.additionalInfo = listScraper(
        sections, 'Нэмэлт мэдээлэл')
    advertisement.location = singleItemScraper(sections, 'Бусад', 'Байршил')
    advertisement.level = singleItemScraper(sections, 'Бусад', 'Түвшин')
    advertisement.type = singleItemScraper(sections, 'Бусад', 'Төрөл')
    minSalary, maxSalary, isDealable = salaryScraper(
        singleItemScraper(sections, 'Бусад', 'Цалин'))
    advertisement.minSalary = minSalary
    advertisement.maxSalary = maxSalary
    advertisement.isDealable = isDealable
    advertisement.address = singleItemScraper(sections, 'Холбоо барих', 'Хаяг')
    advertisement.phoneNumber = singleItemScraper(
        sections, 'Холбоо барих', 'Утас')
    advertisement.fax = singleItemScraper(
        sections, 'Холбоо барих', 'Факс')
    advertisement.adAddedDate = singleItemScraper(
        sections, 'Зарын хугацаа', 'Зар нийтлэсэн огноо')
    print(advertisement.roles)
    print(advertisement.requirements)
    print(advertisement.additionalInfo)
    print(advertisement.location)
    print(advertisement.level)
    print(advertisement.type)
    print(advertisement.minSalary)
    print(advertisement.maxSalary)
    print(advertisement.isDealable)
    print(advertisement.address)
    print(advertisement.phoneNumber)
    print(advertisement.fax)
    print(advertisement.adAddedDate)

    print('SINGLE AD SCRAPPING DONE!!!', url)

    return advertisement
