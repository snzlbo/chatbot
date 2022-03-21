from .classTypes import Advertisement, Category, OtherInfo
from .scrape import UseBeautifulSoup as useScrape


def freeTextScrapper(sections, key, item=None) -> list:
    for section in sections:
        content = []
        subTitle = section.find('h2', class_=None).text
        if key != subTitle:
            continue
        div = section.find('div', class_=None)
        children = div.next_element

        while(children != None):
            try:
                if not hasNotAttribute(children.name):
                    content.append(children.text.strip())
                if children.name == None and children.previous_sibling != None:
                    i = content.index(children.previous_sibling.text)
                    children.previous_sibling.append(' ')
                    children.previous_sibling.append(children.text.strip())
                    content.pop(i)
                    content.append(
                        children.previous_sibling.text.replace('\xa0', ''))
                    children = children.next_sibling
                    continue
            except:
                print('An exception occurred')
            content.append(children.text.replace('\xa0', ''))
            children = children.next_sibling

        return([s for s in filter(listFunc, content)])


def hasNotAttribute(name):
    if name == 'p' or name == 'ul' or name == 'ol':
        return False
    return True


def listFunc(e):
    return len(e) != 0
    return


def essentialScrapper(sections) -> OtherInfo:
    tempOtherInfo = OtherInfo

    for section in sections:
        subTitle = section.find('h2', class_=None).text
        if subTitle != 'Бусад':
            continue
        div = section.find_all('div', class_=None)
        for item in div:
            if item.next_element.text == 'Байршил':
                tempOtherInfo.location = item.find('span').text
            if item.next_element.text == 'Түвшин':
                tempOtherInfo.level = item.find('span').text
            if item.next_element.text == 'Төрөл':
                tempOtherInfo.type = item.find('span').text
            if item.next_element.text == 'Цалин':
                tempOtherInfo.salary = item.find('span').text

    return tempOtherInfo


def advertisementScrape(url) -> Advertisement:
    print(url)
    soup = useScrape(url)
    advertisement = Advertisement(url, soup.find('h3').text.strip())
    sections = soup.find_all('div', class_='section')
    advertisement.roles = freeTextScrapper(
        sections, 'Гүйцэтгэх үндсэн үүрэг')
    advertisement.requirements = freeTextScrapper(
        sections, 'Ажлын байранд тавигдах шаардлага')
    advertisement.additionalInfo = freeTextScrapper(
        sections, 'Нэмэлт мэдээлэл')
    advertisement.otherInfo = essentialScrapper(sections)
    print('roles:', advertisement.roles)
    print('requirements:', advertisement.requirements)
    print('additional Info:', advertisement.additionalInfo)
    print('location:', advertisement.otherInfo.location)
    print('salary:', advertisement.otherInfo.salary)
    print('type:', advertisement.otherInfo.type)
    print('level:', advertisement.otherInfo.level)

    return advertisement
