from flask import Flask
from models import initDB

app = Flask(__name__)

initDB()

from app import routes
