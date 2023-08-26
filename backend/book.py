from flask import Flask
from flask_restful import Resource, Api
import cluster

app = Flask("BookAPI")
api = Api(app)

class Book(Resource):
    def get(self, id):
        if id == 'all':
            return cluster.MakeBooksList()
        intid = int(id)
        rec = cluster.Recommend(intid, 5)
        return rec

api.add_resource(Book, '/books/<id>')