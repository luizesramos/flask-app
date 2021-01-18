from flask import Flask
from routes.raw import raw_routes

app = Flask(__name__)
app.register_blueprint(raw_routes)


@app.route('/')
def home():
    return ''


if __name__ == '__main__':
    app.run()
