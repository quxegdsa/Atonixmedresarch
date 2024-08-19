from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from auth.models import db, User, Post

def setup_admin(app):
    admin = Admin(app, name='My Admin', template_mode='bootstrap3')

    # Add administrative views here
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))