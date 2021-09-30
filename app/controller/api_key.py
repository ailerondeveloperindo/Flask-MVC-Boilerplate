from flask import jsonify, abort
from model.api_key_model import Api_key_Model

class API_Key:
    def __init__(self):
        api_key_obj = Api_key_Model()
        self.api_key = api_key_obj.get_api_key()

    # API_KEY Class checks if api_key is valid. Sends HTTPException 400 if invalid
    def check_api_key(self, api_key_input):
        if api_key_input != self.api_key:
            print("Error : Invalid API Key")
            abort(400)