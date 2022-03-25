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
        return 'None'
    return ' '.join(content)


def textStrip(text) -> str:
    pattern = re.compile('[\r\n\xa0 ]+', re.MULTILINE | re.IGNORECASE)
    return pattern.sub(' ', text.strip())


def hasNotAttribute(name):
    if name == 'p' or name == 'ul' or name == 'ol':
        return False
    return True


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
    k = re.split(r'[^\d,]+', salary, 2, re.IGNORECASE)
    if len(k) < 2:
        [a] = k[0:1]
        return a, a
    [a, b] = k[0:2]
    return a, b


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
    minSalar, maxSalary = salaryScraper(
        singleItemScraper(sections, 'Бусад', 'Цалин'))
    advertisement.minSalary = minSalar
    advertisement.maxSalary = maxSalary
    advertisement.address = singleItemScraper(sections, 'Холбоо барих', 'Хаяг')
    advertisement.phoneNumber = singleItemScraper(
        sections, 'Холбоо барих', 'Утас')
    advertisement.fax = singleItemScraper(
        sections, 'Холбоо барих', 'Факс')
    advertisement.adAddedDate = singleItemScraper(
        sections, 'Зарын хугацаа', 'Зар нийтлэсэн огноо')
    print(advertisement.minSalary, advertisement.maxSalary)
    print('SINGLE AD SCRAPPING DONE!!!', url)

    return advertisement
