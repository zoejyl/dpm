from app import app
from flask import request, Response
import json

@app.route('/', methods=['GET'])
def index():
    return Response("OK", status=200);

