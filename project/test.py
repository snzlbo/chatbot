from misc.adScrape import advertisementScrape as useAdScrape

# https://www.zangia.mn/job/_1dxjbkbf9p
# strong exception https://www.zangia.mn/job/_2ysd8y3e1h
tempAdItem = useAdScrape('https://www.zangia.mn/job/_ju+3ifyu07')

# [['a'], ['c'], 'a']

# print('a', div, 'b')
# print(div.__dict__)
# print([k.text for k in div.find_all('strong')])
# t = div.next_element
# print(t)
# dict = {}
# a = None
# while(t != None):
#   if t.name == 'strong':
#     a = t.text
#   if t.name == None:
#     dict[a] = t.text
#   t = t.next_sibling
#   print(dict)
