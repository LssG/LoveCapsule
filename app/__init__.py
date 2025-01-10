from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../couple_diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 修改jinja2模板语法
app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'

db = SQLAlchemy(app)

from app import routes, models