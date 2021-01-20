from flask import Blueprint, render_template

test_routes = Blueprint('test_routes', __name__, template_folder='templates')

dataset = [
    ('Super Man', 'DC'),
    ('Spider Man', 'Marvel'),
    ('Wonder Woman', 'DC'),
    ('Batman', 'DC'),
    ('Ironman', 'Marvel'),
    ('Cat Woman', 'DC'),
]


@test_routes.route('/test')
def test():
    return render_template('test.html', dataset=dataset)
