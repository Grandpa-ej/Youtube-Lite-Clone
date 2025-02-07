# project/app.py

from flask import Flask, Blueprint
from project.main import main  # Import the main blueprint

def create_app():
    # Create the Flask app instance
    app = Flask(__name__)

    # Register the blueprint with the app
    app.register_blueprint(main)

    return app
