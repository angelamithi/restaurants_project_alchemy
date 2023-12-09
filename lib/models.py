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
    
    review=relationship('Review', backref='restaurant')
    customers=relationship('Customer', secondary='restaurants_customers', back_populates='restaurants')

    def all_restaurants_reviews(self):
        return self.review
    
    def all_restaurant_customers(self):
        return self.customers
    
    def full_restaurant_reviews(self):
        return f"Review for {self} by {self.customers}: {self.review} stars."
    
    @classmethod
    def fanciest(cls):
         return session.query(cls).order_by(cls.price.desc()).first()
        
     
    def __repr__(self):
        return f'<Restaurant {self.name}>'


class Customer(Base):
    __tablename__='customers'
    id=Column(Integer(), primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    review=relationship('Review', backref='customer')
    restaurants=relationship('Restaurant', secondary='restaurants_customers', back_populates='customers')

    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    
    def all_customer_reviews(self):
          return self.review
    def all_customers_restaurants(self):
          return self.restaurants
    def full_name(self):
         return f"{self.first_name} {self.last_name}"
    def favorite_restaurant(self):
         max_review = max(self.review, key=lambda review: review.rating)
         return max_review.restaurant
    def add_review(self,restaurant,rating):
         new_review=Review(rating=rating,customer=self,restaurant=restaurant)
         session.add(new_review)
         self.review.append(new_review)
         session.commit()
         print(f"New review for {self.restaurants} added successfully!")

    def delete_reviews(self,restaurant):
        session.query(Review).filter_by(restaurant_id=restaurant.id).delete()
        session.commit()
        print(f'Review for {restaurant} deleted successfully')


    def __repr__(self):
        return f'<Customer {self.first_name} {self.last_name}>'


class Review(Base):
    __tablename__='reviews'
    id=Column(Integer(),primary_key=True)
    rating=Column(Float())
    customer_id=Column(Integer(), ForeignKey('customers.id'))
    restaurant_id=Column(Integer(),ForeignKey('restaurants.id'))
    
    def __init__(self,rating,customer,restaurant):
        self.rating=rating
        self.customer=customer
        self.restaurant=restaurant

    def customer_review(self):
        return self.customer
    def restaurant_review(self):
        return  self.restaurant
    def full_review(self):
        return f"Review for {self.restaurant} by {self.customer}: {self.rating} stars."

    def __repr__(self):
        return f'< Review {self.rating}>'


  
    
restaurants_customers=Table(
    'restaurants_customers',
    Base.metadata,
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True,
)
   

   

engine=create_engine('sqlite:///restaurants.db')

Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()


retrieved_review= session.query(Review).filter_by(id=1).first()
review_customer=retrieved_review.customer_review()
print(f"Customer who left review 1:{review_customer}")

retrieved_review1 = session.query(Review).filter_by(id=1).first()
review_restaurant=retrieved_review1.restaurant_review()
print(f"Restaurant that was rated in review 1:{review_restaurant}")

restaurant_reviews=session.query(Restaurant).filter_by(id=1).first()
restaurant1_reviews=restaurant_reviews.all_restaurants_reviews()
for  review in restaurant1_reviews:
    print(f'Reviews for restaurant 1: {review.rating}')

restaurant_customers=session.query(Restaurant).filter_by(id=1).first()
restaurant1_customers=restaurant_customers.all_restaurant_customers()
for  customer in restaurant1_customers:
    print(f'Restaurant 1 customers: {customer}')

reviews_for_customer=session.query(Customer).filter_by(id=3).first()
reviews_for_customer3=reviews_for_customer.all_customer_reviews()
for review in reviews_for_customer3:
    print(f"Reviews left by Customer 3: {review}")

restaurants_for_customer=session.query(Customer).filter_by(id=3).first()
customer3_restaurants=restaurants_for_customer.all_customers_restaurants()
for restaurant in customer3_restaurants:
   print(f"Customer 3 retaurants: {restaurant.name}")

newCustomer=Customer("Angela","Mithi")
print(f"Concatenated name: {newCustomer.full_name()}")

fav_restaurant=session.query(Customer).filter_by(id=5).first()
customer5_fav_restaurant=fav_restaurant.favorite_restaurant()
print(f"Customer 5 favorite restaurant is:{customer5_fav_restaurant}")

session.query(Review).filter_by(restaurant_id=6).delete()
session.commit()
restaurant7=session.query(Restaurant).filter_by(id=7).first()
customer9=session.query(Customer).filter_by(id=9).first()
customer9.add_review(restaurant7, 6.5)

restaurant8=session.query(Restaurant).filter_by(id=8).first()
customer7=session.query(Customer).filter_by(id=7).first()
customer7.delete_reviews(restaurant8)

print_full_review=session.query(Review).filter_by(id=10).first()
print(print_full_review.full_review())

fanciest_restaurant = Restaurant.fanciest()
print(f"The fanciest restaurant is:{fanciest_restaurant}")

restaurant3=session.query(Restaurant).filter_by(id=3).first()
restaurant3.full_restaurant_reviews()
print(restaurant3.full_restaurant_reviews())