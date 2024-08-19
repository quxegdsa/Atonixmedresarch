from flask import Flask
from auth.admin import setup_admin
from auth.user import setup_user
from auth.models import db

app = Flask(__name__)

# Setup database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Setup admin dashboard
setup_admin(app)

# Setup user routes
setup_user(app)

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)