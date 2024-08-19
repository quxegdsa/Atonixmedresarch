from flask import Blueprint

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def home():
    return 'Hello, User!'

def setup_user(app):
    app.register_blueprint(user_bp)