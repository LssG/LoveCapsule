from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import sqlite3
from werkzeug.utils import secure_filename

# 配置 Flask 应用
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# 初始化 SQLite 数据库
def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS moments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                image_path TEXT
            )
        ''')

init_db()

# 路由：主页
@app.route('/')
def index():
    return render_template('index.html')

# 路由：上传页面
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        description = request.form['description']
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # 存储到数据库
            with sqlite3.connect('database.db') as conn:
                conn.execute('INSERT INTO moments (description, image_path) VALUES (?, ?)',
                             (description, filepath))
            return jsonify({'status': 'success', 'message': 'Uploaded successfully'})
    return render_template('upload.html')

# 路由：获取图片
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2704 , debug=True)