# This file will serve as the entry point for our Flask application

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to the Stock Dashboard"


if __name__ == "__main__":
    app.run(debug=True)