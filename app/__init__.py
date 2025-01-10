import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../couple_diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 配置上传文件的存储路径
app.config['UPLOAD_FOLDER'] = 'app/static/uploads'
if os.path.exists(app.config['UPLOAD_FOLDER']) is False:
    os.makedirs(app.config['UPLOAD_FOLDER'])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制上传文件大小为 16MB

# 修改jinja2模板语法
app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'

db = SQLAlchemy(app)

from app import routes, models