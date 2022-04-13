from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from dbConnection import db, session
from assets.classTypes import Advertisement, Category

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    _id = Column(String, primary_key=True)
    url = Column(String, nullable=False)
    name = Column(String, nullable=False)
    parent_id = Column(String, ForeignKey('category._id'), nullable=False)

    def __init__(self, category: Category) -> None:
        self._id = category.id
        self._url = category.url
        self.name = category.name
        self._id = category.id



class Advertisement(Base):
    __tablename__ = 'advertisememnt'

    _id = Column(String, primary_key=True)
    category_id = Column(String, ForeignKey(
        'category._id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    url = Column(String(200), nullable=False)
    company = Column(String(200))
    title = Column(String(200), nullable=False)
    comp = Column(String(200))
    roles = Column(String)
    requirements = Column(String)
    additionalInfo = Column(String)
    city = Column(String)
    district = Column(String)
    exactAddress = Column(String)
    level = Column(String)
    type = Column(String)
    minSalary = Column(Float)
    maxSalary = Column(Float)
    isDealable = Column(Boolean)
    phoneNumber = Column(String)
    fax = Column(String)
    publishedDate = Column(DateTime)
    category = relationship('Category', backref='category')


def create():
    Base.metadata.create_all(db)


create()
