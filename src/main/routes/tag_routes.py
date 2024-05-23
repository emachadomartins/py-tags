from flask import Blueprint, request, jsonify

routes = Blueprint('tags_routes', __name__)

@routes.route('/create_tag', methods=['POST'])
def create_tags():
    print(request.json)
    return jsonify({ "resp": "ok" }), 200
