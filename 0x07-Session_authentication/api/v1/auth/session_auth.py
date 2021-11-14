#!/usr/bin/env python3
""" SessionAuth inherits from Auth """
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ SessionAuth class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a Session ID for a user_id """
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns a User ID based on a Session ID """
        if not session_id or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ returns a User instance based on a cookie value: """
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        user = User.get(user_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ deletes the user session / logout """
        if not request:
            return False
        cookie = self.session_cookie(request)
        if not cookie:
            return False
        if not self.user_id_for_session_id(cookie):
            return False
        del self.user_id_by_session_id[cookie]
        return True
