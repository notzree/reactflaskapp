from flask import Flask
from flask_cors import CORS
from flask import jsonify
from flask import request, Response
from supabaseConnect import get_all_users, create_embedding
app = Flask(__name__)
CORS(app)
@app.route("/profile")
def home():
    response_body = {
        "name": "Richard Zhang",
        "bio": "Ur mom"
    }
    return response_body

@app.route("/")
def getUsers():
    data =  get_all_users()
    return data

@app.route("/create_embedding", methods= ['POST'])
def createEmbedding():
    data = request.get_json()
    resp = create_embedding()
    return resp
 
    






