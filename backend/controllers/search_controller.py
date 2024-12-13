from flask import Blueprint, jsonify, request
from services.search_service import get_all_searches

search_bp = Blueprint('search', __name__)

@search_bp.route('/searches', methods=['GET'])
def get_searches():
    data = get_all_searches()
    return jsonify(data), 200

@search_bp.route('/create', methods=['POST'])
def create():
    return {"error": "Method not implemented"}, 501

@search_bp.route('/update', methods=['PUT'])
def update():
    return {"error": "Method not implemented"}, 501

@search_bp.route('/delete', methods=['DELETE'])
def delete():
    return {"error": "Method not implemented"}, 501




