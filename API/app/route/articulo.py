from http import HTTPStatus
from flask import Blueprint, jsonify, request
import service.articles as article_service
#from flasgger import swag_from
#from api.model.welcome import WelcomeModel
#from api.schema.welcome import WelcomeSchema

article_route = Blueprint('articulo', __name__, url_prefix='/articles')

@article_route.route('/', methods=['GET'])
def get_all_articles():
    result = article_service.get_all_articles()
    return jsonify(result)

@article_route.route('/<int:id>', methods=['GET'])
def get_article_by_id(id: int):
    result = article_service.get_article_by_id(id)
    return jsonify[result], 200

@article_route.route('/', methods=['POST'])
def create_article():
    article = request.get_json()
    result = article_service.create_article(article)
    return result, 200

@article_route.route('/<int:id>', methods=['PUT'])
def update_article(id: int):
    article = request.get_json()
    result = article_service.update_article(id, article)
    return result, 200

@article_route.route('/<int:id>', methods=['DELETE'])
def delete_article(id: int):
    article = request.get_json()
    result = article_service.delete_article(id)
    return article, 200

