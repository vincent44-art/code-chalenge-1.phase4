from server.app import db, create_app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    # Reset the database
    db.drop_all()
    db.create_all()

    # Create restaurants
    r1 = Restaurant(name="Kiki's Pizza", address="123 Pizza Lane")
    r2 = Restaurant(name="Mama's Pizza", address="456 Tomato Blvd")

    # Create pizzas
    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Hawaiian", ingredients="Ham, Pineapple")

    # Add to session
    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    # Create restaurant-pizza relationships
    rp1 = RestaurantPizza(price=5, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=7, pizza_id=p2.id, restaurant_id=r2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()

    print("✅ Database seeded successfully!")
