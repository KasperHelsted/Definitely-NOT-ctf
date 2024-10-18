#!/usr/bin/env python3
from flask import Flask, request, Response, make_response, redirect, url_for
import json, os
from Crypto.Cipher import AES

# Global variables
app = Flask(__name__)

secret_key = os.urandom(16)
auth_cookie_nonce = os.urandom(8)


# Generate a secure cookie using AES-128 encryption
def gen_cookie(role):
    pt = role.encode()
    cipher = AES.new(secret_key, AES.MODE_CTR, nonce=auth_cookie_nonce)
    ct = cipher.encrypt(pt).hex()
    return ct


def decrypt_cookie(cookie):
    ct = bytes.fromhex(cookie)
    cipher = AES.new(secret_key, AES.MODE_CTR, nonce=auth_cookie_nonce)
    pt = cipher.decrypt(ct)
    return pt


@app.route('/flag')
def retPsyduck():
    user_cookie = request.cookies.get('permissions')
    if user_cookie is None:
        return Response("No cookie set")

    try:
        decrypted = decrypt_cookie(user_cookie)
    except:
        return Response("Something went wrong decrypting your cookie")

    if decrypted == b'Admin':
        with open('images/flag.png', 'rb') as f:
            return Response(f.read(), mimetype='image/png')
    else:
        return Response(f"This page is for admins only! Your cookie says: {decrypted.hex()}")


# /login route
@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')

    # Admin login
    if password == secret_key.hex():
        res = make_response(redirect(url_for('index')))
        # Set Admin cookie
        cookie = gen_cookie("Admin")
        res.set_cookie('permissions', cookie)
        return res

    # cool guys account
    elif password == "psyduck4ever":
        res = make_response(redirect(url_for('index')))
        # Set Admin cookie
        cookie = gen_cookie("Killerdog")
        res.set_cookie('permissions', cookie)
        return res

    # Guest stub for incorrect passwords
    else:
        res = make_response(redirect(url_for('index')))
        cookie = gen_cookie("Guest")
        res.set_cookie('permissions', cookie)
        return res


# /logout route
@app.route('/logout')
def logout():
    res = make_response(redirect(url_for('index')))
    res.delete_cookie('permissions')  # Delete the cookie
    return res


@app.route('/')
def index():
    user_cookie = request.cookies.get('permissions')
    res = make_response()

    if user_cookie is None:
        # User does not have a cookie, show the login form
        with open('./templates/index.html') as f:
            res.set_data(f.read().replace("{{login_or_logout}}", '''
                <form action="/login" method="POST">
                    <input type="password" name="password" placeholder="Enter password" required>
                    <button type="submit" class="button-5">Login</button>
                </form>
            '''))
        return res

    # Check cookie to greet user correctly
    try:
        decrypted = decrypt_cookie(user_cookie)
    except:
        return Response("Something went wrong decrypting your cookie")

    try:
        decrypted = decrypted.decode()
    except:
        return Response(
            f"Error: failed to decode user: {decrypted.hex()}. Try deleting your cookies if this continues ")

    # User has a cookie, show the logout button
    with open('./templates/index.html') as f:
        res.set_data(f.read().replace("{{login_or_logout}}", f'''
        <span> Welcome {decrypted} </span>  <button onclick="location.href='/logout'" class="button-5">Logout</button>
        '''))
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0')