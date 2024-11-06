import os
import pickle
import json
import sqlite3
from flask import Flask, request, jsonify, render_template
from workflow import (create_database, google_drive_files, fetch_data,
                         process_audio, insert_data, insert_video_audio_data)

app = Flask(__name__)

# Initialize the database
create_database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio_endpoint():
    audio_file = request.files['audio']
    language = request.form.get('language', 'en')
    audio_path = os.path.join('uploads', audio_file.filename)
    audio_file.save(audio_path)

    output = process_audio(audio_path, language)
    
    if output:
        return jsonify(output), 200
    else:
        return jsonify({"error": "Processing failed"}), 400

@app.route('/fetch_data', methods=['GET'])
def fetch_data_endpoint():
    max_chars = int(request.args.get('max_chars', 10))
    data = fetch_data(max_chars)
    return jsonify(data), 200

@app.route('/insert_video_audio_data', methods=['POST'])
def insert_video_audio_data_endpoint():
    # Extract the data from the request
    data = request.get_json()

    # Validate the input data
    if not all(k in data for k in ('id', 'file_name_video', 'url_video', 'file_name_audio', 'url_audio')):
        return jsonify({"error": "Missing required fields"}), 400

    id = data['id']
    file_name_video = data['file_name_video']
    url_video = data['url_video']
    file_name_audio = data['file_name_audio']
    url_audio = data['url_audio']
    
    # Insert the data into the database
    insert_video_audio_data(id, file_name_video, url_video, file_name_audio, url_audio)
    
    return jsonify({"message": "Video and audio data inserted successfully."}), 200


@app.route('/insert_data', methods=['POST'])
def insert_data_endpoint():
    # Extract the data from the request
    data = request.get_json()

    # Validate the input data
    if not all(k in data for k in ('id', 'file_name_video', 'file_name_audio', 'url_video', 'url_audio', 'transcript')):
        return jsonify({"error": "Missing required fields"}), 400

    id = data['id']
    file_name_video = data['file_name_video']
    file_name_audio = data['file_name_audio']
    url_video = data['url_video']
    url_audio = data['url_audio']
    transcript = data['transcript']

    # Insert the data into the database
    insert_data(file_name_video, file_name_audio, url_video, url_audio, transcript, id)
    
    return jsonify({"message": "Data inserted successfully."}), 200

@app.route('/google_drive', methods=['POST'])
def google_drive_endpoint():
    folder_id = request.form['folder_id']
    google_drive_files(folder_id)
    return jsonify({"message": "Files processed successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
