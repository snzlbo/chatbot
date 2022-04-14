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
    parent_id = Column(String, ForeignKey('category._id'), nullable=True)


def create():
    Base.metadata.create_all(db)


def insert(category: Category, parentId=None):
    session.add(PCategory(_id=category.id, url=category.url,
                name=category.name, parent_id=parentId))
    session.commit()

# session.add()
# categories = session.query(PCategory).filter(PCategory._id == 'b.17').first()
# session.merge(categories)
# if categories != None:
#     print(categories.name)
# else:
#     print('None')
# for category in categories:
#     print(category.name)
