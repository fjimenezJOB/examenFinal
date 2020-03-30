from pymongo import MongoClient

# Mongo URL Atlas
MONGO_URL_ATLAS = 'mongodb+srv://franjimenez:Francisco1231998@develop-0hasi.mongodb.net/test?authSource=admin&replicaSet=develop-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)
db = client['Web_Scraping']
collection = db['informe_rural']

def subirLinks(link):
    collection = db['linksHoteles']
    collection.insert_one({'link' : link})

