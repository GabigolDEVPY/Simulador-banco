from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__,template_folder='../../templates')


@home_bp.route('/home', methods=["GET"])
def return_home():
    return render_template('home.html')