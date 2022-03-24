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
                # if children.name == None and children.previous_sibling != None:
                #     print(children.name)
                #     i = content.index(children.previous_sibling.text)
                #     children.previous_sibling.append(' ')
                #     children.previous_sibling.append(children.text.strip())
                #     content.pop(i)
                #     content.append(
                #         children.previous_sibling.text.replace('\xa0', ''))
                #     children = children.next_sibling
                #     continue
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


def advertisementScrape(url) -> Advertisement:
    print(url)
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
    advertisement.salary = singleItemScraper(sections, 'Бусад', 'Цалин')
    advertisement.address = singleItemScraper(sections, 'Холбоо барих', 'Хаяг')
    advertisement.phoneNumber = singleItemScraper(
        sections, 'Холбоо барих', 'Утас')
    advertisement.fax = singleItemScraper(
        sections, 'Холбоо барих', 'Факс')
    advertisement.adAddedDate = singleItemScraper(
        sections, 'Зарын хугацаа', 'Зар нийтлэсэн огноо')
    print('company:', advertisement.company)
    print('title:', advertisement.title)
    print('roles:', advertisement.roles)
    print('requirements:', advertisement.requirements)
    print('additional Info:', advertisement.additionalInfo)
    print('location:', advertisement.location)
    print('salary:', advertisement.salary)
    print('type:', advertisement.type)
    print('level:', advertisement.level)
    print('address:', advertisement.address)
    print('phone:', advertisement.phoneNumber)
    print('fax:', advertisement.fax)
    print('adAddedDate:', advertisement.adAddedDate)

    return advertisement
