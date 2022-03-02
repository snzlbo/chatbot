from .classTypes import Advertisement, Category
from .scrape import UseBeautifulSoup as useScrape


def findAdTitle(sections, key) -> str:
    for section in sections:
        subTitle = section.find('h2', class_=None).text
        div = section.find('div', class_=None)
        ul = div.find_all('ul')
        p = div.find_all('p')
        if ul != []:
            print('in ul')
            for li in ul:
                print(li)
        if p != []:
            print('in p')
            for li in ul:
                print(li)


def advertisementScrape(url) -> Advertisement:
    soup = useScrape(url)
    advertisement = Advertisement(url, soup.find('h3').text.strip())
    sections = soup.find_all('div', class_='section')
    findAdTitle(sections, 'Гүйцэтгэх үндсэн үүрэг')
    return advertisement
