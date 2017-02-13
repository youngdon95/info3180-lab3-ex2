from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret keyjbkhbk'
from app import views