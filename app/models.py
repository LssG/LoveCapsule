from app import db

class DiaryEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, date, image, description):
        self.date = date
        self.image = image
        self.description = description

    def __repr__(self):
        return f"DiaryEntry('{self.date}', '{self.image}', '{self.description}')"