class Category:
    id = None
    url = ''
    name = ''

    def __init__(self, url, name, parentCategory=None) -> None:
        self.url = url
        self.name = name
        self.parentCategory = parentCategory

    def getUrl(self) -> str:
        return self.url


class Location:
    city = ''
    district = ''
    exactAddress = ''

    def __init__(self, city=None, district=None, exactAddress=None) -> None:
        self.city = city
        self.district = district
        self.exactAddress = exactAddress


class Contact:
    phoneNumber = ''
    fax = ''


class Advertisement:
    category = Category
    url = ''
    company = ''
    title = ''
    level = ''
    type = ''
    minSalary = ''
    maxSalary = ''
    isDealable = ''
    location = Location
    roles = ''
    requirements = ''
    additionalInfo = ''
    contact = Contact
    adAddedDate = ''

    def __init__(self, url, title) -> None:
        self.url = url
        self.title = title

    def setSalary(self, minSalary, maxSalary, isDealable) -> None:
        self.minSalary = minSalary
        self.maxSalary = maxSalary
        self.isDealable = isDealable

    def setCategory(self, category) -> None:
        self.category = category

    def setLocation(self, location) -> None:
        self.location = location

    def setContact(self, contact) -> None:
        self.contact = contact
