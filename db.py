# DB setting to be added here
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create_engine(type_of_sqlserver://user:password@host:port/database)

engine = create_engine('postgresql://postgres:postgres123@localhost:5432/flask_db', echo=False)
Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

