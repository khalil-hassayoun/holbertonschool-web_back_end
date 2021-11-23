#!/usr/bin/env python3
"""
Main file
"""


from flask import json
import requests


def register_user(email: str, password: str) -> None:
    """Testing register end-point"""
    payload = {
        "email": email,
        "password": password
    }
    res = requests.post("{}/users".format(URL), data=payload)
    assert res.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """Testing login end-point"""
    payload = {
        "email": email,
        "password": password
    }
    res = requests.post("{}/sessions".format(URL), data=payload)
    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """Testing login end-point"""
    payload = {
        "email": email,
        "password": password
    }
    res = requests.post("{}/sessions".format(URL), data=payload)
    assert res.status_code == 200
    return res.cookies.get('session_id')


def profile_unlogged() -> None:
    """Testing not logged profile end-point"""
    res = requests.get("{}/profile".format(URL))
    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """Testing logged profile end-point"""
    cookies = {
        "session_id": session_id
    }
    res = requests.get("{}/profile".format(URL), cookies=cookies)
    assert res.status_code == 200


def log_out(session_id: str) -> None:
    """Testing logout end-point"""
    cookies = {
        "session_id": session_id
    }
    res = requests.delete("{}/sessions".format(URL), cookies=cookies)
    assert res.status_code == 200


def reset_password_token(email: str) -> str:
    """Testing reset password end-point"""
    payload = {
        "email": email
    }
    res = requests.post("{}/reset_password".format(URL), data=payload)
    assert res.status_code == 200
    payload = json.loads(res.content)
    return payload["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Testing update password end-point"""
    payload = {
        "email": email,
        "new_password": new_password,
        "reset_token": reset_token
    }
    r = requests.put("/reset_password".format(URL), data=payload)
    assert r.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
URL = "http://localhost:5000"

if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
