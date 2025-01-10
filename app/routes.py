from flask import Flask, render_template, request, jsonify
from app import app, db
from app.models import DiaryEntry

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
        data = request.json
        if data is None or 'date' not in data or 'image' not in data or 'description' not in data:
            return jsonify({'error': 'Invalid request data!'}), 400
        new_entry = DiaryEntry(
            date=data['date'],
            image=data['image'],
            description=data['description']
        )
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'message': 'Entry added successfully!'}), 201
    return jsonify({'error': 'Invalid request method!'}), 405

@app.route('/api/entries/<int:id>', methods=['DELETE'])
def delete_entry(id):
    entry = DiaryEntry.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message': 'Entry deleted successfully!'}), 200