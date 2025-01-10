from app import db

class DiaryEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(100), nullable=False)  # 存储图片路径
    description = db.Column(db.Text, nullable=False)

    # 重写构造函数
    def __init__(self, date, image, description):
        # 确保父类的构造函数被调用
        super(DiaryEntry, self).__init__()
        self.date = date
        self.image = image
        self.description = description

    def __repr__(self):
        return f"DiaryEntry('{self.date}', '{self.image}', '{self.description}')"