from .classTypes import Advertisement, Category
from .scrape import UseBeautifulSoup as useScrape


def findAdTitle(sections, key) -> list:
    for section in sections:
        content = []
        subTitle = section.find('h2', class_=None).text
        if key != subTitle:
            continue
        div = section.find('div', class_=None)
        children = div.next_element

        while(children != None):
            if children.name == None:
                i = content.index(children.previous_sibling.text)
                content[i] = children.previous_sibling.append(
                    children.text.strip())
                print(children.previous_sibling.text)
                children = children.next_sibling
                continue

            content.append(children.text.replace('\xa0', ''))
            children = children.next_sibling

        return([s for s in filter(a, content)])


def a(e):
    return len(e) != 0


def advertisementScrape(url) -> Advertisement:
    print(url)
    soup = useScrape(url)
    advertisement = Advertisement(url, soup.find('h3').text.strip())
    sections = soup.find_all('div', class_='section')
    advertisement.roles = findAdTitle(
        sections, 'Гүйцэтгэх үндсэн үүрэг')
    advertisement.requirements = findAdTitle(
        sections, 'Ажлын байранд тавигдах шаардлага')
    print('roles:', advertisement.roles)
    print('requirements:', advertisement.requirements)
    return advertisement
