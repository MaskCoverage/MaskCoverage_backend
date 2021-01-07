import os
import sys

from flask import Flask, jsonify, request, abort, send_file
import json
#import requests
from demo import main as save_img

app = Flask(__name__, static_url_path="")


def save_predict_img():
    save_img("./data/test.jpg")

@app.route("/show-img", methods=["GET"])
def show_img():
    return send_file(save_img("./data/test.jpg"), mimetype="image/jpg")

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
    #save_predict_img()