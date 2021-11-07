#!/usr/bin/env python3
""" module to manage the API authentication """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Public method """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        if path[-1] == '/' and path[:-1] in excluded_paths:
            return False
        if path[-1] != '/' and path + '/' in excluded_paths:
            return False
        for exp in excluded_paths:
            if exp[-1] == "*" and path.startswith(exp[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Public method """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ Public method """
        return None
