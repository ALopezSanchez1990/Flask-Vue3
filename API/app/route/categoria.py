from http import HTTPStatus
from flask import Blueprint, jsonify, request
import service.category as category_service
#from flasgger import swag_from
#from api.model.welcome import WelcomeModel
#from api.schema.welcome import WelcomeSchema

categoria_route = Blueprint('categoria', __name__, url_prefix='/category')

@categoria_route.route('/', methods=['GET'])
def get_all_categories():
    result = category_service.get_all_categories()
    return jsonify(result)
    
@categoria_route.route('/<int:id>', methods=['GET'])
def get_category_by_id(id: int):
    return f'hola articles by id {id}', 200

@categoria_route.route('/', methods=['POST'])
def create_category():
    article = request.get_json()
    return article, 200

@categoria_route.route('/<int:id>', methods=['PATCH'])
def update_category(id: int):
    article = request.get_json()
    return article, 200

@categoria_route.route('/<int:id>', methods=['DELETE'])
def delete_category(id: int):
    article = request.get_json()
    return article, 200