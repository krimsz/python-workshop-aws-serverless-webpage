from random import randint
from flask import Flask, render_template, request
import app.data_utils as data_utils

app = Flask(__name__)

class ValidationError(Exception):
    pass


MIN_ITEMS = 1
MAX_ITEMS = 100
DEFAULT_MOVIES_COUNT = 2


def validate_n_items(n_items):
    if n_items < MIN_ITEMS or n_items > MAX_ITEMS:
        raise ValidationError()



@app.route('/')
def hello_world():
    n_items = int(request.args.get('n_movies') or DEFAULT_MOVIES_COUNT)
    validate_n_items(n_items)
    template_index = randint(1, 2)
    movies = data_utils.select_n_rows(n_items)
    return render_template('index_{0}.html'.format(template_index), rows=movies)


@app.errorhandler(ValidationError)
def handle_bad_request(e):
    return 'Bad Request!', 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
