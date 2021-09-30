from pymongo import MongoClient
from config import Config

class Youtube_Model:

    def __init__(self):
        cfg = Config()
        # initialize a Mongo Client Object
        self.mongo_client = MongoClient(cfg.DATABASE_HOST,cfg.DATABASE_HOST_PORT)
        
        # initialize an object that points to 'config' Collection on db_config Database
        # 'config' collection stores Youtube Data API Key
        self.cfg = self.mongo_client['db_config']['config']

    def get_devkey(self):
        # retrieve dan returns api_key from Config Collection
        return self.cfg.find_one()['youtube_data_api_key']
