from local_settings import my_db
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
db = create_engine(my_db)
base = declarative_base()

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
