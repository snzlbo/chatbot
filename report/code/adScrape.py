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
        sections, 'Guitsetgeh undsen uurerg')
    advertisement.requirements = listScraper(
        sections, 'Ajliin bairnii shaardlaga')
    advertisement.additionalInfo = listScraper(
        sections, 'Nemelt medeelel')
    advertisement.level = singleItemScraper(sections, 'Busad', 'Tuvshin')
    advertisement.type = singleItemScraper(sections, 'Busad', 'Turul')
    minSalary, maxSalary, isDealable = salaryScraper(
        singleItemScraper(sections, 'Busad', 'Tsalin'))
    city, district = locationScrapper(
        singleItemScraper(sections, 'Busad', 'Bairshil'))
    advertisement.minSalary = minSalary
    advertisement.maxSalary = maxSalary
    advertisement.isDealable = isDealable
    advertisement.city = city
    advertisement.district = district
    advertisement.address = singleItemScraper(sections, 'Холбоо барих', 'Хаяг')
    advertisement.phoneNumber = singleItemScraper(
        sections, 'Holboo barih', 'Utas')
    advertisement.fax = singleItemScraper(
        sections, 'Holboo barih', 'Fax')
    advertisement.adAddedDate = singleItemScraper(
        sections, 'Zariin hugatsaa', 'Zar niitelsen ognoo')
    print(advertisement.additionalInfo)
    print('SINGLE AD SCRAPPING DONE!!!', url)

    return advertisement
