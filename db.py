from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True, nullFalse=False)
    shares = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return '<Stock %r>' % self.symbol


# Add stock data
def init_db():
    with db.engine.connect() as conn:
        conn.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
    db.create_all()