# backend/database/api_database_app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

# Get correct database path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) # 
DB_PATH = os.path.join(CURRENT_DIR, 'video_database.db')

# print(__file__)  
# # Output: "D:/DEPLOY1.3.2_SHOWUIMENTOR/backend/database/api_database_app.py"

# print(os.path.abspath(__file__))
# # Output: "D:/DEPLOY1.3.2_SHOWUIMENTOR/backend/database/api_database_app.py"

# print(CURRENT_DIR)
# # Output: "D:/DEPLOY1.3.2_SHOWUIMENTOR/backend/database"

# print(DB_PATH)
# # Output: "D:/DEPLOY1.3.2_SHOWUIMENTOR/backend/database/video_database.db"

# backend/database/api_database_app.py


@app.route('/get_video_data', methods=['GET'])
def get_video_data():
    video_url = request.args.get('url')
    
    try:
        # Connect to database using the correct path
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        print(f"Connected to database at: {DB_PATH}")  # Debug print
        
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
                'criteria': result[2]
            })
        
        return jsonify({'error': 'Video not found'}), 404

    except Exception as e:
        print(f"Error accessing database: {e}")  # Debug print
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    print(f"Starting server...")
    print(f"Database location: {DB_PATH}")
    app.run(debug=True, port=3000)