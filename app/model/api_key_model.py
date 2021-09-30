from pymongo import MongoClient
from config import Config

class Api_key_Model:

    def __init__(self):
        cfg = Config()
        # initialize a Mongo Client Object
        self.mongo_client = MongoClient(cfg.DATABASE_HOST,cfg.DATABASE_HOST_PORT)
        
        # initialize an object that points to 'config' Collection on db_config Database
        # 'config' collection stores Service's API Key
        self.cfg = self.mongo_client['db_config']['config']

    def get_api_key(self):
        # retrieve dan returns api_key from Config Collection
        return self.cfg.find_one()['api_access_key']
