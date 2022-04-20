from re import L
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from assets.classTypes import Advertisement, Category
from connection import Base, db, session


class PCategory(Base):
    __tablename__ = 'category'

    _id = Column(String, primary_key=True)
    url = Column(String, nullable=False)
    name = Column(String, nullable=False)
    parent_id = Column(String,
                       ForeignKey('category._id',
                                  onupdate='CASCADE',
                                  ondelete='CASCADE'),
                       nullable=True)
    category = relationship('PCategory')

    def __init__(self, category: Category):
        self._id = category.id
        self.url = category.url
        self.name = category.name
        if category.parentCategory != None:
            self.parent_id = category.parentCategory.id
        else:
            self.parent_id = None


class PAdvertisement(Base):
    __tablename__ = 'advertisement'

    _id = Column(String, primary_key=True)
    category_id = Column(String,
                         ForeignKey('category._id',
                                    onupdate='CASCADE',
                                    ondelete='CASCADE'),
                         nullable=False)
    url = Column(String, nullable=False)
    company = Column(String)
    title = Column(String)
    roles = Column(String)
    requirements = Column(String)
    additionalInfo = Column(String)
    city = Column(String)
    district = Column(String)
    exactAddress = Column(String)
    level = Column(String)
    types = Column(String)
    minSalary = Column(Float)
    maxSalary = Column(Float)
    isDealable = Column(Boolean)
    phoneNumber = Column(String)
    fax = Column(String)
    publishedDate = Column(DateTime)
    category = relationship('PCategory')

    def __init__(self, advertisement: Advertisement):
        self._id = advertisement.id
        self.category_id = advertisement.category.id
        self.url = advertisement.url
        self.company = advertisement.company
        self.title = advertisement.title
        self.roles = advertisement.roles
        self.requirements = advertisement.requirements
        self.additionalInfo = advertisement.additionalInfo
        self.city = advertisement.location.city
        self.district = advertisement.location.district
        self.exactAddress = advertisement.location.exactAddress
        self.level = advertisement.level
        self.types = advertisement.type
        self.minSalary = advertisement.minSalary
        self.maxSalary = advertisement.maxSalary
        self.isDealable = advertisement.isDealable
        self.phoneNumber = advertisement.contact.phoneNumber
        self.fax = advertisement.contact.fax
        self.publishedDate = advertisement.adAddedDate


def createDB():
    Base.metadata.create_all(db)


def insertToCategory(category: Category):
    session.add(PCategory(category))


def insertToAdvertisement(advertisement: Advertisement):
    session.add(PAdvertisement(advertisement))


def upsertCategory(category: Category):
    if(category.parentCategory != None):
        upsertCategory(category.parentCategory)
    row = session.query(PCategory).filter(PCategory._id == category.id)
    if row.first() == None:
        if category.parentCategory != None:
            insertToCategory(category, category.parentCategory.id)
        else:
            insertToCategory(category, None)
    else:
        dict = PCategory(category).__dict__
        del dict['_sa_instance_state']
        row.update(dict, synchronize_session=False)
    session.commit()
    print(category.id, 'CATEGORY UPSERT DONE')


def upsertAdvertisement(advertisement: Advertisement):
    row = session.query(PAdvertisement).filter(
        PAdvertisement._id == advertisement.id)
    if row.first() == None:
        insertToAdvertisement(advertisement)
    else:
        dict = PAdvertisement(advertisement).__dict__
        del dict['_sa_instance_state']
        row.update(dict, synchronize_session=False)
    session.commit()
    print(advertisement.id, 'ADVERTISEMENT UPSERT DONE')


createDB()
