from array import array
from .regex import UseRegex as useRegex
from .scrape import UseBeautifulSoup as useScrape

def createLinkList(pagination) -> array:
  linkList = []
  total = int(useRegex(pagination.find_all('a')[-1]['href']))
  
  i = 1
  for i in range(total):
    url = 'https://www.zangia.mn/job/list/b.4/r.442/pg.' + str(i)
    linkList.append(url)
  return linkList
