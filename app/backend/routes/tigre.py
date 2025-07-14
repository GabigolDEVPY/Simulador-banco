from flask import Blueprint, render_template

tigre_bp = Blueprint("tigre", __name__, template_folder="../../templates/tigre")

@tigre_bp.route('/tigre', methods=["GET"])
def return_tiger_page():
    return render_template("tigre.html")