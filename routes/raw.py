from flask import Blueprint, redirect, url_for

# This is how we can distribute flask routes across different files
# Instead of Flask, we use a Blueprint that mut be registered with the app
# e.g.,
# import my_app.raw_routes as raw_routes
# app = Flask(__name__)
# app.register_blueprint(raw_routes)

raw_routes = Blueprint('raw_routes', __name__, template_folder='templates')


@raw_routes.route('/raw/<name>')  # route has argument
def raw(name):
    return f'<h1>Raw HTML {name}</h1>'


@raw_routes.route('/raw/')  # ending / is a separate route
def raw_empty():
    return redirect(url_for('raw_routes.raw', name='empty'))


@raw_routes.route('/raw')  # ending in no slash is a third route
def raw_admin():
    return redirect(url_for('raw_routes.raw', name='admin'))
