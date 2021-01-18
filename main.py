from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return ''


@app.route('/raw/<name>')  # route has argument
def raw(name):
    return f'<h1>Raw HTML {name}</h1>'


@app.route('/raw/')  # ending / is a separate route
def raw_admin():
    return redirect(url_for('raw', name='empty'))


@app.route('/raw')  # ending in no slash is a third route
def raw_admin():
    return redirect(url_for('raw', name='admin'))


if __name__ == '__main__':
    app.run()
