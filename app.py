from flask import Flask, request, redirect, url_for, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///love_capsule.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 数据库模型
class Capsule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(300), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# 首页路由：返回前端瀑布流数据
@app.route('/')
def index():
    return render_template('index.html')

# 获取点滴数据（JSON）
@app.route('/api/capsules', methods=['GET'])
def get_capsules():
    capsules = Capsule.query.order_by(Capsule.created_at.desc()).all()
    data = [
        {
            "title": capsule.title,
            "content": capsule.content,
            "image_path": capsule.image_path,
            "created_at": capsule.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        for capsule in capsules
    ]
    return jsonify(data)

# 添加点滴页面和逻辑
@app.route('/add', methods=['GET', 'POST'])
def add_capsule():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image = request.files.get('image')
        image_path = None
        if image:
            upload_folder = os.path.join('static', 'uploads')
            os.makedirs(upload_folder, exist_ok=True)
            image_path = os.path.join(upload_folder, image.filename)
            image.save(image_path)

        new_capsule = Capsule(title=title, content=content, image_path=image_path)
        db.session.add(new_capsule)
        db.session.commit()
        return redirect(url_for('index'))  # 添加点滴后重定向到首页
    
    return render_template('add.html')


# 初始化数据库
# db.create_all()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=2704, debug=True)
