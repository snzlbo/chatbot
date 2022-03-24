from misc.adScrape import advertisementScrape as useAdScrape

# https://www.zangia.mn/job/_1dxjbkbf9p
# strong exception https://www.zangia.mn/job/_2ysd8y3e1h
tempAdItem = useAdScrape('https://www.zangia.mn/job/_23oxogj9va')

print(type(tempAdItem.roles))
print(type(tempAdItem.requirements))
print(type(tempAdItem.additionalInfo))
print(type(tempAdItem.fax))
