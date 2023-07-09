from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from celery_app import upload_to_s3
import time, os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'message': 'Empty filename provided'}), 400
    
    try:
        filename = secure_filename(file.filename)
        file_format = os.path.splitext(filename)[1]
        key = 'images/' + str(int(time.time())) + file_format
        
        upload_to_s3.delay(file.read(), key)
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
    return jsonify({'message': 'Success'})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
