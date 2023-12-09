#models.py
from sqlalchemy import create_engine, Column, Integer, String, Table,Float,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

Base=declarative_base()



class Restaurant(Base):
    __tablename__='restaurants'
    id=Column(Integer(), primary_key=True)
    name=Column(String())
    price=Column(Float())
    review=relationship('Review', backref='rest')
    customers=relationship('Customer', secondary='restaurants_customers', back_populates='restaurants')


class Customer(Base):
    __tablename__='customers'
    id=Column(Integer(), primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    review=relationship('Review', backref='cust')
    restaurants=relationship('Restaurant', secondary='restaurants_customers', back_populates='customers')


class Review(Base):
    __tablename__='reviews'
    id=Column(Integer(),primary_key=True)
    rating=Column(Float())
    customer_id=Column(Integer(), ForeignKey('customers.id'))
    restaurant_id=Column(Integer(),ForeignKey('restaurants.id'))

    def customer(self):
        return self.customer_id
    def restaurant(self):
        return self.restaurant_id
    
restaurants_customers=Table(
    'restaurants_customers',
    Base.metadata,
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True,
)
   

   

engine=create_engine('sqlite:///restaurants.db')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()

