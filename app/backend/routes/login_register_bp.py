
from flask import Blueprint, render_template

login_register_bp = Blueprint('login_register', __name__,template_folder='../../templates/login-register')

@login_register_bp.route('/', methods=["GET"])
def return_home():
    return render_template('login.html')


@login_register_bp.route('/register', methods=["GET"])
def return_register_page():
    return render_template('register.html')