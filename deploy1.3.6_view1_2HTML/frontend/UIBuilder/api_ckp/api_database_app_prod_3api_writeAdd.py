# backend/database/api_database_app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Get correct database path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(CURRENT_DIR, 'database/video_database.db')


# print(__file__)  
# # Output: "D:/DEPLOY1.3.2_SHOWUIMENTOR/backend/database/api_database_app.py"

# print(os.path.abspath(__file__))
# # Output: "D:/DEPLOY1.3.2_SHOWUIMENTOR/backend/database/api_database_app.py"

# print(CURRENT_DIR)
# # Output: "D:/DEPLOY1.3.2_SHOWUIMENTOR/backend/database"

# print(DB_PATH)
# # Output: "D:/DEPLOY1.3.2_SHOWUIMENTOR/backend/database/video_database.db"


# Existing get_video_data route remains the same
@app.route('/get_video_data', methods=['GET'])
def get_video_data():
    url_video = request.args.get('url')
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT url_video, transcription, criteria
            FROM videos 
            WHERE url_video = ?
        ''', (url_video,))
        
        result = cursor.fetchone()
        
        if result:
            return jsonify({
                'url_video': result[0],
                'transcript': result[1],
                'criteria': result[2]
            })
        
        return jsonify({'error': 'Video not found'}), 404

    except Exception as e:
        print(f"Error accessing database: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

# New route to save scores
@app.route('/save_score', methods=['POST'])
def save_score():
    try:
        data = request.json
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Create scores table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url_video TEXT NOT NULL,
                criteria TEXT NOT NULL,
                score INTEGER NOT NULL,
                note TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Insert new score
        cursor.execute('''
            INSERT INTO scores (url_video, criteria, score, note, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            data['url_video'],
            data['criteria'],
            data['score'],
            data.get('note', ''),  # Use empty string if note is not provided
            datetime.now().isoformat()
        ))
        
        conn.commit()
        
        return jsonify({
            'message': 'Score saved successfully',
            'id': cursor.lastrowid
        }), 201

    except Exception as e:
        print(f"Error saving score: {e}")
        conn.rollback()  # Rollback transaction if error occurs
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

# New route to get scores for a specific video
@app.route('/get_scores', methods=['GET'])
def get_scores():
    url_video = request.args.get('url_video')
    
    if not url_video:
        return jsonify({'error': 'url_video parameter is required'}), 400
        
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, url_video, criteria, score, note, timestamp
            FROM scores
            WHERE url_video = ?
            ORDER BY timestamp DESC
        ''', (url_video,))
        
        rows = cursor.fetchall()
        
        scores = [{
            'id': row[0],
            'url_video': row[1],
            'criteria': row[2],
            'score': row[3],
            'note': row[4],
            'timestamp': row[5]
        } for row in rows]
        
        return jsonify(scores)

    except Exception as e:
        print(f"Error fetching scores: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(port=3000, debug=True)