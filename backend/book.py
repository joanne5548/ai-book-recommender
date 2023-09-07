from flask import Flask
import cluster

app = Flask("BookAPI")

@app.route('/books', methods=['GET'])
def GetAllBooks():
    return cluster.MakeBooksList()

@app.route('/books/<id>', methods=['GET'])
def GetBookObject(id):
    return cluster.IDToBook(id, cluster.MakeBooksList())

@app.route('/recommend/<id>', methods=['GET'])
def ReccomendBooks(id):
    return cluster.Recommend(id, 10)
