from misc.pagination import createLinkList as createLinkList
from ntpath import join
import re
import csv
from datetime import date
from misc.adScrape import advertisementScrape as useAdScrape
from misc.scrape import UseBeautifulSoup as useScrape
from misc.classTypes import Category

# strong exception https://www.zangia.mn/job/_2ysd8y3e1h
tempAdItem = useAdScrape('https://www.zangia.mn/job/_7mt11zl7tl')
