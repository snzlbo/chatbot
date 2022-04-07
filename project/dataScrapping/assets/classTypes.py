class Category:
    url = ''
    name = ''

    def __init__(self, url, name, parentId=None) -> None:
        self.url = url
        self.name = name
        self.parentId = parentId

    def getUrl(self) -> str:
        return self.url


class location:
    city = ''
    district = ''
    exactAddress = ''

    def __init__(self, city=None, district=None, exactAddress=None) -> None:
        self.city = city
        self.district = district
        self.exactAddress = exactAddress


class contact:
    phoneNumber = ''
    fax = ''


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
    city = ''
    district = ''
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
