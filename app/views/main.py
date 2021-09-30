# Main View

from flask import Blueprint, jsonify
from controller.sample_controller import Sample_Controller

main = Blueprint('main', __name__)
sample_ctrl = Sample_Controller()

@main.route("/", methods = ['GET'])
def request():
    return jsonify(
        response = "Connected"
    )
