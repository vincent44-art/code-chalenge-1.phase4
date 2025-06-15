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