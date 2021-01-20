from flask import Flask, redirect, url_for

from routes.raw import raw_routes
from routes.test import test_routes

app = Flask(__name__)
app.register_blueprint(raw_routes)
app.register_blueprint(test_routes)


@app.route('/')
def home():
    return redirect(url_for('test_routes.test'))


if __name__ == '__main__':
    app.run()
