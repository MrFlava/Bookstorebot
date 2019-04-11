import os
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
if not os.getenv('sqlalchemy.url'):
    from src.settings import PROJECT_ROOT
    import configparser
    config = configparser.ConfigParser()
    config.read(os.path.join(PROJECT_ROOT, 'botmanlib.ini'))
    os.environ['sqlalchemy.url'] = config['botmanlib']['sqlalchemy.url']
from botmanlib.models import db
base = db.Base
db = create_engine(db.database_url)
class Products(base):
    __tablename__ = 'sell'
    __table_args__ = {'extend_existing': True}
    id_book = Column(Integer, primary_key=True)
    prod_name = Column(String)
    about = Column(String)
    cost = Column(Integer)
    edition = Column(Integer)

class Users(base):
    __tablename__ = 'botusers'
    __table_args__ = {'extend_existing': True}
    user_id = Column(Integer, primary_key=True)
    name = Column(String)

class Orderbooks(base):
    __tablename__ = 'orderedbooks'
    __table_args__ = {'extend_existing': True}
    nickname = Column(String, primary_key=True)
    bookname = Column(String)
    email = Column(String)
    phone = Column(Integer)

Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)
