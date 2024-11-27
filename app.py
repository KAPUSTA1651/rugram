from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 500
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 501
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500 


if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#   return 'test! Good'

# if __name__ == 'main':
#   app.run(host= '0.0.0.0', port=3000)