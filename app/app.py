from flask import Blueprint, Flask
from backend.routes.login_register_bp import login_register_bp

def CreateApp():
    app = Flask(__name__)
    app.register_blueprint(login_register_bp)
    return app

app = CreateApp()

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)