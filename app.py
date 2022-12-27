from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/api/authors", methods = ['POST'])
def create_author():
    author = request.get_json()
    
    name = author['name']
    
    return name

@app.route("/api/authors/<id>", methods = ['PUT'])
def update_author(id):
    author = request.json

    name = author['name']

    return name
    
@app.route("/api/authors", methods = ['GET'])
def get_all_authors():
    return "All authors"

@app.route("/api/authors/<id>", methods = ['GET'])
def get_author(id):
    return id

@app.route("/api/books", methods = ["GET"])
def get_all_books():
    return "All books"

@app.route("/api/books/<id>", methods = ["GET"])
def get_book(id):
    return id

@app.route("/api/books", methods = ["POST"])
def create_book():
    book = request.json
    
    name = book['name']
    
    return name
