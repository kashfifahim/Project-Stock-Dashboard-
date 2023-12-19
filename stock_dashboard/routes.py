from flask import jsonify
from .db import Stock
from .alpha_vantage import get_stock_price

def register_routes(app):
    @app.route('/')
    def index():
        return "Welcome to the Stock Dashboard!"

    @app.route('/api/stocks')
    def get_stocks():
        stocks = Stock.query.all()
        stock_data = []
        for stock in stocks:
            price = get_stock_price(stock.symbol)
            stock_data.append({'symbol': stock.symbol, 'shares': stock.shares, 'price': price})
        return jsonify(stock_data)