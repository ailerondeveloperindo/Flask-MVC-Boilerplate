# Main View

from flask import Blueprint, jsonify
from controller.sample_controller import Sample_Controller

main = Blueprint('main', __name__)
sample_ctrl = Sample_Controller()

@main.route("/", methods = ['GET'])
def request(api_key):
    return jsonify(
        response = "This is a sample REST API"
    )
