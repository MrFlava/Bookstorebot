from local_settings import my_db
from sqlalchemy import create_engine
from  sqlalchemy import Column, String
from  sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.declarative import declarative_base
db = create_engine(my_db)
base = declarative_base()
class Books(base):
    __tablename__ = 'products'

    title = Column(String,primary_key=True)
    description = Column(String)
    price = Column(String)

Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)
books = session.query(Books)
