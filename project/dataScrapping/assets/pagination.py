from array import array
from .regex import UseRegex as useRegex
from .scrape import UseBeautifulSoup as useScrape


def createLinkList(pagination, url) -> array:
    linkList = []
    total = int(useRegex(pagination.find_all('a')[-1]['href']))

    for i in range(total + 1):
        if i == 0:
            continue
        link = url + '/pg.' + str(i)
        linkList.append(link)
    return linkList
