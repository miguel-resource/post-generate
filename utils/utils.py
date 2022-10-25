from pymongo import MongoClient
from environs import Env

env = Env()
env.read_env()

def mongo_posts(name_database):
    client = MongoClient(env("MONGO_URI"))
    db = client.postsDB

    if name_database == 'pets':
        collection = db.posts_pets

    return collection