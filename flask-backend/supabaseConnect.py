import os
from supabase_py import create_client, Client
from flask import jsonify
from flask import request, Response
import cohere 

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def get_all_users():
    d = supabase.table('users').select("*").execute()
    return jsonify(d)

#Creates the embedding using co:here and stores it into the PGVector Postgres Database
def create_embedding():
    data = request.get_json()
    try:
        text = data['body']
        print(text)
        co = cohere.Client(os.environ.get("COHERE_KEY"))
        embeds = co.embed(texts=[text],model = 'large', truncate= 'START').embeddings

        supabaseData = supabase.table('embeddings').insert({"title":text, "embedding": embeds[0]}).execute()
        return supabaseData
    except:
        return Response('''{"message": "Bad Request"}''', status=400)

    





