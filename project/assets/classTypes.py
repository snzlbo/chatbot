class Category:
    url = ''
    name = ''
    parentId = ''

    def __init__(self, url, name, parentId='None') -> None:
        self.url = url
        self.name = name
        self.parentId = parentId

    def getUrl(self) -> str:
        return self.url


class Advertisement:
    category = Category
    url = ''
    company = ''
    title = ''
    # ListInfo
    roles = ''
    requirements = ''
    additionalInfo = ''
    # OtherInfo
    location = ''
    level = ''
    type = ''
    minSalary = ''
    maxSalary = ''
    isDealable = ''
    # ContactInfo
    address = ''
    phoneNumber = ''
    fax = ''
    adAddedDate = ''

    def __init__(self, url, title) -> None:
        self.url = url
        self.title = title

    def setCategory(self, category) -> None:
        self.category = category
