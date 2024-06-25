import datetime

from faker import Faker
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

fake = Faker()

# ბაზის მონაცემები
HOST = "localhost"
PORT = 5432
DATABASE = "it_step_new"
USER = "postgres"
PASSWORD = "Dori1313"

engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

Base = declarative_base()


class Country(Base):
    __tablename__ = "Country"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))


class City(Base):
    __tablename__ = "cities"

    cityid = Column(Integer, primary_key=True, autoincrement=True)
    cityname = Column(String(15))



class Customers(Base):
    __tablename__ = "customers"
    custumersid = Column(Integer, primary_key=True, autoincrement=True)
    idnumber = Column(String(15))
    last_name = Column(String(20))
    first_name = Column(String(30))
    cityid = Column(Integer, foreign_key="cities.cityid")
    income = Column(Float)
    create_date = Column(DateTime, default=datetime.date)
    update_date = Column(DateTime, default=datetime.date)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
