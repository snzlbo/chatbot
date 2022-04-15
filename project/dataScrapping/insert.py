import sys
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from assets.classTypes import Category
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
    category = relationship('PCategory', backref='category')


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
    types = Column(String)
    isDealable = Column(Boolean)
    phoneNumber = Column(String)
    fax = Column(String)
    publishedDate = Column(DateTime)
    category = relationship('PCategory', backref='category')


def create():
    Base.metadata.create_all(db)


def insertToCategory(category: Category, parentId=None):
    session.add(PCategory(_id=category.id, url=category.url,
                name=category.name, parent_id=parentId))
    session.commit()


create()
