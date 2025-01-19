from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_Database='postgresql://postgres:password@localhost:5432/Blog_App'

engine=create_engine(URL_Database)


SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()
