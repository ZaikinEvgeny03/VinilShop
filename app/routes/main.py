from flask import render_template, Blueprint
from app.models.vinyl import Vinyl

main = Blueprint('main', __name__)

@main.route('/')
def index():
    vinyls = Vinyl.query.all()
    return render_template('index.html', vinyls=vinyls)
