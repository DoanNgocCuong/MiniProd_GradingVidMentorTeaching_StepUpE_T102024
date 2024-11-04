from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # This allows browser to request data

@app.route('/get_video_data', methods=['GET'])
def get_video_data():
    video_url = request.args.get('url')
    
    try:
        # Connect to database
        conn = sqlite3.connect('video_database.db')
        cursor = conn.cursor()
        
        # Get data for this URL
        cursor.execute('''
            SELECT video_url, transcription, criteria
            FROM video_transcripts 
            WHERE video_url = ?
        ''', (video_url,))
        
        result = cursor.fetchone()
        
        if result:
            return jsonify({
                'video_url': result[0],
                'transcript': result[1],
                'criteria': result[2]  # It's already JSON string in DB
            })
        
        return jsonify({'error': 'Video not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)