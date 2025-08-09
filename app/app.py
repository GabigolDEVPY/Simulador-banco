import sys
sys.dont_write_bytecode = True
from flask import Flask
from backend.routes.login_register_bp import login_register_bp
from backend.routes.home_bp import home_bp
from backend.routes.transfer import transfer_bp
from backend.routes.invest import invest_bp
from backend.routes.pig import pig_bp
from backend.routes.tigre import tigre_bp

def CreateApp():
    app = Flask(__name__)
    app.secret_key = '82934bfd74g78ufd2b4ufbw4b'
    app.register_blueprint(login_register_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(transfer_bp)
    app.register_blueprint(invest_bp)
    app.register_blueprint(pig_bp)
    app.register_blueprint(tigre_bp)
    return app

app = CreateApp()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5500)