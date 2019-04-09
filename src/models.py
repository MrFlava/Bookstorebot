import os
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
if not os.getenv('sqlalchemy.url'):
    from settings import PROJECT_ROOT
    import configparser
    config = configparser.ConfigParser()
    config.read(os.path.join(PROJECT_ROOT, 'botmanlib.ini'))
    os.environ['sqlalchemy.url'] = config['botmanlib']['sqlalchemy.url']
from botmanlib.models import db
base = db.Base
db = create_engine(db.database_url)
class Products(base):
    __tablename__ = 'sell'

    id_book = Column(Integer, primary_key=True)
    prod_name = Column(String)
    about = Column(String)
    cost = Column(Integer)
    edition = Column(Integer)

class Users(base):
    __tablename__ = 'botusers'
    user_id = Column(Integer, primary_key=True)
    name = Column(String)

class Orderbooks(base):
    __tablename__ = 'orderedbooks'
    nickname = Column(String, primary_key=True)
    bookname = Column(String)
    email = Column(String)
    phone = Column(Integer)

Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)