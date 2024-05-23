from flask import Flask
from src.main.routes.tag_routes import routes as tag_routes

server = Flask(__name__)

server.register_blueprint(tag_routes)
