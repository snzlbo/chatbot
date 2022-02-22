from .classTypes import Advertisement, Category
from .scrape import UseBeautifulSoup as useScrape

def advertisementScrape(url) -> Advertisement:
  soup = useScrape(url)
  advertisement = Advertisement(url, soup.find('h3').text.strip())
  return advertisement