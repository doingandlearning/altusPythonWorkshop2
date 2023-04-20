from functools import wraps
from flask import jsonify, request

def with_header_auth(func):
    @wraps(func)
    def decorated_func(*arg, **kwargs):
        auth_key = request.headers['x-api-key']
        if auth_key == "super-secret-key":
            return func(*arg,**kwargs)
        return jsonify({"message": "Auth key required"}), 403
    return decorated_func