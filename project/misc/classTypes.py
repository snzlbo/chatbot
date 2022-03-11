class Category:
    url = ''
    name = ''
    parentId = ''

    def __init__(self, url, name, parentId=None) -> None:
        self.url = url
        self.name = name
        self.parentId = parentId

    def getUrl(self) -> str:
        return self.url


class ContactInfo:
    address = ''
    phoneNumber = ''
    fax = ''

    def __init__(self, address=None, phoneNumber=None, fax=None) -> None:
        self.address = address
        self.phoneNumber = phoneNumber
        self.fax = fax


class OtherInfo:
    location = ''
    level = ''
    type = ''
    salary = ''

    def __init(self, location=None, level=None, type=None, salary=None) -> None:
        self.location = location
        self.level = level
        self.type = type
        self.salary = salary


class Advertisement:
    url = ''
    title = ''
    category = Category
    roles = []
    requirements = []
    additionalInfo = []
    otherInfo = OtherInfo
    contactInfo = ContactInfo

    def __init__(self, url, title) -> None:
        self.url = url
        self.title = title

    def setCategory(self, category) -> None:
        self.category = category
