from turtle import pos
from flask import (
    Flask,
    Blueprint
)
from flask_restx import Api
from pymongo import MongoClient

# routes
from routes.posts import (
    posts_namespace,
    GetPosts,
    CreatePosts
)

app = Flask(__name__)
blueprint = Blueprint("api", __name__, url_prefix="/posts-markdown")
api = Api(
    blueprint,
    doc='/doc',
    version='1.0',
    title='Posts Markdow',
    description='Geneador de contenido para blogs'
)
mongoclient = MongoClient('localhost')
app.register_blueprint(blueprint)

###################
#    NAMESPACE    #
###################
api.add_namespace(posts_namespace)

##################
#    RESOURCE    #
##################
posts_namespace.add_resource(GetPosts, "list-posts")
posts_namespace.add_resource(CreatePosts, "create-post")

if __name__ == "__main__":
    app.run(debug=True)