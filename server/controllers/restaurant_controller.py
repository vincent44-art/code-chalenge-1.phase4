from flask import Blueprint, jsonify, request
from server.app import db
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

restaurant_bp = Blueprint('restaurant_bp', __name__, url_prefix='/restaurants')


@restaurant_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    result = [
        {"id": r.id, "name": r.name, "address": r.address}
        for r in restaurants
    ]
    return jsonify(result), 200


@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    pizzas = [
        {
            "id": rp.pizza.id,
            "name": rp.pizza.name,
            "ingredients": rp.pizza.ingredients
        }
        for rp in restaurant.restaurant_pizzas
    ]
    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": pizzas
    }), 200


@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204