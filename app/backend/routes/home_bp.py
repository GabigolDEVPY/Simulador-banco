
from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity


home_bp = Blueprint('home', __name__,template_folder='../../templates')


@home_bp.route('/home', methods=["GET"])
@jwt_required()
def return_home():
    usuario = get_jwt_identity()
    return render_template('home.html')


@home_bp.route('/nofify', methods=["GET"])
def return_notify():
    return render_template('notify.html')


@home_bp.route('/history', methods=["GET"])
def return_history():
    return render_template('history.html')


