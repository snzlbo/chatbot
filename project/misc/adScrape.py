from .classTypes import Advertisement, Category, OtherInfo
from .scrape import UseBeautifulSoup as useScrape


def freeTextScrapper(sections, key) -> list:
    for section in sections:
        content = []
        subTitle = section.find('h2', class_=None).text
        if key != subTitle:
            continue
        div = section.find('div', class_=None)
        ul = div.find_all('li', class_=None)
        p = div.find_all('p', class_=None)

        # simple list or paragraph scrape
        if ul != []:
            for li in ul:
                content.append(li.text.replace('\xa0', ''))
            return([s for s in filter(listFunc, content)])

        if p != []:
            for pr in p:
                content.append(pr.text.replace('\xa0', ''))
            return([s for s in filter(listFunc, content)])

        # other free text scrapping
        children = div.next_element
        print(children)

        while(children != None):
            print(children.name)
            if children.name == None:
                print(children.name)
                i = content.index(children.previous_sibling.text)
                children.previous_sibling.append(' ')
                children.previous_sibling.append(children.text.strip())
                content.pop(i)
                content.append(
                    children.previous_sibling.text.replace('\xa0', ''))
                children = children.next_sibling
                continue

            content.append(children.text.replace('\xa0', ''))
            children = children.next_sibling

        return([s for s in filter(listFunc, content)])


def listFunc(e):
    return len(e) != 0


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
