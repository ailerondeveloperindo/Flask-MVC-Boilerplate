from pymongo import MongoClient
from config import Config

# This is sample model which fetch data from a MongoDB database

class Sample_Model:

    def __init__(self):
        cfg = Config()
        # initialize a Mongo Client Object
        self.mongo_client = MongoClient(cfg.DATABASE_HOST,cfg.DATABASE_HOST_PORT)
        
        # initialize an object that points to 'config' Collection on db_config Database
        self.cfg = self.mongo_client['db_config']['config']