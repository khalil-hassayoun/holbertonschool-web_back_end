#!/usr/bin/env python3
""" Module of Index views
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    """
    email = request.form.get("email")
    if not email or email == '':
        return jsonify({"error": "email missing"}), 400
    password = request.form.get("password")
    if not password or password == '':
        return jsonify({"error": "password missing"}), 400
    objs = User().search({"email": email})
    if not objs or objs == []:
        return jsonify({"error": "no user found for this email"}), 404
    if not objs[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(objs[0].id)
    result = jsonify(objs[0].to_json())
    result.set_cookie(os.getenv("SESSION_NAME"), session_id)
    return result


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """ DELETE /api/v1/auth_session/logout
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
