from functools import wraps
from flask import session, abort

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "login" not in session:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function