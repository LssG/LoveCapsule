from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from app import app, db
from app.models import DiaryEntry

# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add_entry_page():
    return render_template('add_entry.html')

@app.route('/api/entries', methods=['GET', 'POST'])
def entries():
    if request.method == 'GET':
        entries = DiaryEntry.query.all()
        return jsonify([{
            'id': entry.id,
            'date': entry.date,
            'image': entry.image,
            'description': entry.description
        } for entry in entries])
    elif request.method == 'POST':
        # 检查是否有文件上传
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename) # type: ignore
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # 获取表单数据
            date = request.form.get('date')
            description = request.form.get('description')

            # 存储到数据库
            new_entry = DiaryEntry(
                date=date,
                image=f'/static/uploads/{filename}',  # 存储图片路径
                description=description
            )
            db.session.add(new_entry)
            db.session.commit()
            return jsonify({'message': 'Entry added successfully!'}), 201
        return jsonify({'error': 'File type not allowed'}), 400
    return jsonify({'error': 'Method not allowed'}), 405

@app.route('/api/entries/<int:id>', methods=['DELETE'])
def delete_entry(id):
    entry = DiaryEntry.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message': 'Entry deleted successfully!'}), 200