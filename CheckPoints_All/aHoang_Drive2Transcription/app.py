import os
import pickle
import json
import sqlite3
from flask import Flask, request, jsonify, render_template
from workflow import (create_database, google_drive_files, fetch_data,
                         process_audio, insert_data, fetch_data_by_url)  

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

@app.route('/google_drive', methods=['POST'])
def google_drive_endpoint():
    folder_id = request.form['folder_id']
    google_drive_files(folder_id)
    return jsonify({"message": "Files processed successfully."}), 200

@app.route('/insert_video_audio_data', methods=['POST'])
def insert_video_audio_data_endpoint():
    try:
        data = request.json
        id = data.get('id')
        file_name_video = data.get('file_name_video')
        url_video = data.get('url_video')
        file_name_audio = data.get('file_name_audio')
        url_audio = data.get('url_audio')

        # Insert the video/audio data into the database
        insert_data(file_name_video, file_name_audio, url_video, url_audio, '', id)
        
        return jsonify({"message": "Video/Audio data inserted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/insert_data', methods=['POST'])
def insert_data_endpoint():
    try:
        data = request.json
        id = data.get('id')
        file_name_video = data.get('file_name_video')
        file_name_audio = data.get('file_name_audio')
        url_video = data.get('url_video')
        url_audio = data.get('url_audio')
        transcript = data.get('transcript')

        # Insert the full data into the database (including transcript)
        insert_data(file_name_video, file_name_audio, url_video, url_audio, transcript, id)
        
        return jsonify({"message": "Data inserted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/fetch_data_by_url', methods=['GET'])
def fetch_data_by_url_endpoint():
    try:
        url = request.args.get('url')
        if not url:
            return jsonify({"error": "URL parameter is required"}), 400

        data = fetch_data_by_url(url)
        
        if not data:
            return jsonify({"message": "No data found for the given URL"}), 404
        
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
