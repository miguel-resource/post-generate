from multiprocessing.spawn import import_main_path
from flask_restx import (
    Namespace,
    Resource
)
from flask.wrappers import Response
from flask import (
    jsonify,
    flash,
    request
)
from utils.utils import mongo_posts
from bson import json_util 
from datetime import datetime 
import markdown

posts_namespace = Namespace (
    'Posts',
    description="Endpoint of posts",
    path="/posts" 
)

responses_dict = {
    200: """{"data": {}, "message": "string"}""",
    400: 'Error de conexión',
    500: 'Error del servidor'
}

class GetPosts(Resource): 
    @posts_namespace.doc(
        description="Get Posts",
        response = responses_dict
    )
    def get(self):
        data = []
        try:
            posts = mongo_posts("pets").find({})
            data = [post for post in posts]

            response = Response(json_util.dumps(data), content_type='application/json')
        except:
            response = jsonify(data)
        return response

class CreatePosts(Resource):
    @posts_namespace.doc(
        description="Creat post",
        response = responses_dict,
        params = {
            "title": {
                'description': 'Título del post',
                'type': 'string',
                'in': 'query',
                'required': 'true'
            },
            "category": {
                'description': 'Categoría del post',
                'type': 'string',
                'in': 'query',
                'required': 'true'
            },
            "description": {
                'description': 'Decripción de la publicación',
                'type': 'string',
                'in': 'query',
                'required': 'true'
            },
            "content": {
                'description': 'Contenido del post',
                'type': 'string',
                'in': 'query',
                'required': 'true'
            }
        }
    )
    def post(self):
        data = {}
        response = {}
        try:
            now = datetime.now()

            data["title"] = request.args.get('title')
            data["date"] = datetime.timestamp(now)
            data["category"] = request.args.get('category')
            data["description"] = request.args.get('description')
            data["content"] = markdown.markdown(request.args.get('content'))

            print(data)
            mongo_posts("pets").insert_one(data)
            response["status"] = 200
            response["message"] = "Post created successfully!"

        except Exception:
            response["status"] = 501
            response["message"] = "Erro to created post! :c"
        return response