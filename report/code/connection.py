from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from local_settings import postgresql as settings
import logging

log = logging.getLogger(__name__)


def get_database():
    try:
        engine = get_engine_from_settings()
        log.info("Connected to PostgreSQL database!")
    except:
        log.exception("Failed to get database connection!")
        return None, 'fail'

    return engine


def get_engine_from_settings():
    keys = ['user', 'password', 'host', 'port', 'db']
    if not all(key in keys for key in settings.keys()):
        raise Exception('Bad config file')

    return get_engine(settings['user'],
                      settings['password'],
                      settings['host'],
                      settings['port'],
                      settings['db'])


def get_engine(user, password, host, port, db):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine


def get_session():
    engine = get_database()
    session = sessionmaker(bind=engine)
    return session()


db = get_database()
session = get_session()
Base = declarative_base()
print(db)
