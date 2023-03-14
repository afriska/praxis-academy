from datetime import timedelta
from flask import Flask, jsonify
from flask_jwt_extended import *
import os

app = Flask(__name__)
jwt = JWTManager(app)

app.config["JWT_SECRET_KEY"] = os.getenv("SALT_PASSWORD")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes=5)

@app.route('/login', methods=["POST"])
def login():
    accessToken = create_access_token(identity="afriska")
    refreshToken = create_refresh_token(identity="afriska")
    return jsonify(accessToken=accessToken, refreshToken=refreshToken)

@app.route('/refresh', methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    accessToken = create_access_token(identity=identity)
    return jsonify(accessToken=accessToken)

@app.route('/protected', methods=["GET"])
@jwt_required()
def protected():
    return jsonify(msg = "berhasil masuk halaman protected")