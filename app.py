# This file will serve as the entry point for our Flask application

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/stockdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        from stock_dashboard.db import db, init_db
        from .db import db, init_db
        db.init_app(app)
        init_db()

    from .routes import register_routes
    register_routes(app)

    return app