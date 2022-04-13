from array import array


def createLinkList(pagination, url) -> array:
    linkList = []
    total = int(splitUrl(pagination.find_all(
        'a')[-1]['href'], 'pg.').split('.')[1])

    for i in range(total + 1):
        if i == 0:
            continue
        link = url + '/pg.' + str(i)
        linkList.append(link)
    return linkList


def splitUrl(input, state):
    pattern = input.split('/')
    if state == 'ad':
        return pattern[-1]
    for item in pattern:
        if item.startswith(state):
            return item
    return 0
