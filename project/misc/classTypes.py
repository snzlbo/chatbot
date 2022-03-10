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

    def __init__(self, address, phoneNumber, fax=None) -> None:
        self.address = address
        self.phoneNumber = phoneNumber
        self.fax = fax


class Advertisement:
    url = ''
    title = ''
    category = Category
    roles = []
    requirements = []
    additionalInfo = []
    location = ''
    level = ''
    type = ''
    salary = ''
    contactInfo = ContactInfo

    def __init__(self, url, title) -> None:
        self.url = url
        self.title = title

    def setCategory(self, category) -> None:
        self.category = category
