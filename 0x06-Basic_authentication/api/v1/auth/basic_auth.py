#!/usr/bin/env python3
""" BasicAuth inherits from Auth """
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth inherits from Auth """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if (
           not authorization_header or
           not isinstance(authorization_header, str) or
           not authorization_header.startswith("Basic ")):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        returns the decoded value of a Base64 string
        base64_authorization_header
        """
        if (
           not base64_authorization_header or
           not isinstance(base64_authorization_header, str)):
            return None
        try:
            return base64.b64decode(base64_authorization_header).decode(
                'utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value
        """
        if (
           not decoded_base64_authorization_header or
           not isinstance(decoded_base64_authorization_header, str) or
           ':' not in decoded_base64_authorization_header):
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ returns the User instance based on his email and password """
        if (
           not user_email or
           not isinstance(user_email, str) or
           not user_pwd or
           not isinstance(user_pwd, str)
           ):
            return None
        objs = User().search({"email": user_email})
        if not objs:
            return None
        if objs[0].is_valid_password(user_pwd):
            return objs[0]
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the User instance for a request """
        if not request:
            return None
        auth_header = Auth().authorization_header(request)
        auth_header = self.extract_base64_authorization_header(auth_header)
        dec_header = self.decode_base64_authorization_header(auth_header)
        cred = self.extract_user_credentials(dec_header)
        return self.user_object_from_credentials(cred[0], cred[1])
