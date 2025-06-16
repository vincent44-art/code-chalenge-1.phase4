from flask import Blueprint, jsonify
from server.models.pizza import Pizza

pizza_bp = Blueprint('pizza_bp', __name__, url_prefix='/pizzas')


@pizza_bp.route('', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    result = [
        {"id": p.id, "name": p.name, "ingredients": p.ingredients}
        for p in pizzas
    ]
    return jsonify(result), 200



    
@pizza_bp.route('/<int:id>', methods=['GET'])
def get_pizza_by_id(id):
    pizza = Pizza.query.get(id)
    if pizza:
        result = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }
        return jsonify(result), 200
    else:
        return jsonify({"error": "Pizza not found"}), 404
    