#seed.py
from models import Restaurant, Customer, Review,session

session.query(Restaurant).delete()
session.query(Customer).delete()
session.query(Review).delete()

session.commit()

restaurants_info=[
  {
    "id": 1,
    "name": "Delicious Delights",
    "price": 25.50
  },
  {
    "id": 2,
    "name": "Savory Spices",
    "price": 18.75
  },
  {
    "id": 3,
    "name": "Gourmet Grains",
    "price": 32.99
  },
  {
    "id": 4,
    "name": "Culinary Corner",
    "price": 21.25
  },
  {
    "id": 5,
    "name": "Tasty Treats",
    "price": 27.80
  },
  {
    "id": 6,
    "name": "Flavorful Fusion",
    "price": 35.45
  },
  {
    "id": 7,
    "name": "Epicurean Eats",
    "price": 29.00
  },
  {
    "id": 8,
    "name": "Palate Pleasers",
    "price": 23.65
  },
  {
    "id": 9,
    "name": "Mouthwatering Morsels",
    "price": 19.99
  },
  {
    "id": 10,
    "name": "Sizzling Sustenance",
    "price": 26.75
  }
]
session.add_all([Restaurant(**restaurant) for restaurant  in restaurants_info])
session.commit()

customers_info=[{
  "id": 1,
  "first_name": "Nananne",
  "last_name": "Stearnes"
}, {
  "id": 2,
  "first_name": "Marietta",
  "last_name": "Maslin"
}, {
  "id": 3,
  "first_name": "Jolynn",
  "last_name": "Hacket"
}, {
  "id": 4,
  "first_name": "Boniface",
  "last_name": "Meiklem"
}, {
  "id": 5,
  "first_name": "Hillery",
  "last_name": "Kaye"
}, {
  "id": 6,
  "first_name": "Giacopo",
  "last_name": "Crannage"
}, {
  "id": 7,
  "first_name": "Stormie",
  "last_name": "Caldwall"
}, {
  "id": 8,
  "first_name": "Briney",
  "last_name": "Traill"
}, {
  "id": 9,
  "first_name": "Nonie",
  "last_name": "Moat"
}, {
  "id": 10,
  "first_name": "Merridie",
  "last_name": "Innerstone"
}]
session.add_all([Customer(**customer) for customer  in customers_info])
session.commit()

review_info=[
  {"id": 1, "rating": 4.3, "customer_id": 3, "restaurant_id": 7},
  {"id": 2, "rating": 5.0, "customer_id": 8, "restaurant_id": 2},
  {"id": 3, "rating": 3.7, "customer_id": 5, "restaurant_id": 9},
  {"id": 4, "rating": 4.8, "customer_id": 2, "restaurant_id": 4},
  {"id": 5, "rating": 2.5, "customer_id": 10, "restaurant_id": 6},
  {"id": 6, "rating": 4.1, "customer_id": 1, "restaurant_id": 3},
  {"id": 7, "rating": 3.9, "customer_id": 9, "restaurant_id": 8},
  {"id": 8, "rating": 4.5, "customer_id": 4, "restaurant_id": 1},
  {"id": 9, "rating": 2.8, "customer_id": 7, "restaurant_id": 5},
  {"id": 10, "rating": 4.0, "customer_id": 6, "restaurant_id": 10}
]
session.add_all([Review(**review) for review in review_info])
session.commit()
