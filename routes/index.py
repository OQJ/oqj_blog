from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,

)
main = Blueprint('index', __name__)

@main.route('/')
def index():
    return render_template('login/login.html')