from flask import Blueprint, render_template, request

test_routes = Blueprint('test_routes', __name__, template_folder='templates')

dataset = [
    ('Super Man', 'DC'),
    ('Spider Man', 'Marvel'),
    ('Wonder Woman', 'DC'),
    ('Batman', 'DC'),
    ('Ironman', 'Marvel'),
    ('Cat Woman', 'DC'),
]


@test_routes.route('/test', methods=['POST', 'GET'])
def test():
    search_term = ''
    if request.method == 'POST' and 'search_term' in request.form:
        search_term = request.form['search_term']
    return render_template('test.html', dataset=dataset, selected_hero=search_term)
