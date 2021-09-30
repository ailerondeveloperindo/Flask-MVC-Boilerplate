# Main View

from flask import Blueprint, jsonify
from controller.youtube import Youtube
from controller.api_key import API_Key

main = Blueprint('main', __name__)
yt_obj = Youtube()
apikey_obj = API_Key()

@main.route("/api/main/api_key=<string:api_key>", methods = ['GET'])
def request(api_key):
    apikey_obj.check_api_key(api_key)
