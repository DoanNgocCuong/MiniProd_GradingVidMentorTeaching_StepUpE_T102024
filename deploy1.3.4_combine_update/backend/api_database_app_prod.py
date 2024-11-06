# backend/database/api_database_app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

# Get correct database path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) # 
DB_PATH = os.path.join(CURRENT_DIR, 'database/video_database.db')

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
    url_video = request.args.get('url')
    
    try:
        # Connect to database using the correct path
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        print(f"Connected to database at: {DB_PATH}")  # Debug print
        
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
        print(f"Error accessing database: {e}")  # Debug print
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()


@app.route('/save_evaluation', methods=['POST'])
def save_evaluation():
    try:
        data = request.json
        print("Received data:", data)  # Debug log
        
        # Validate required fields
        required_fields = ['url_video', 'criteria', 'score', 'note']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Connect to database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # First, create the evaluations table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS evaluations (
                evaluation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                url_video TEXT NOT NULL,
                criteria TEXT NOT NULL,
                score INTEGER CHECK(score >= 0 AND score <= 5),
                note TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(url_video, criteria)
            )
        ''')
        
        # Insert or update evaluation using url_video directly
        cursor.execute('''
            INSERT OR REPLACE INTO evaluations 
            (url_video, criteria, score, note) 
            VALUES (?, ?, ?, ?)
        ''', (
            data['url_video'],
            data['criteria'],
            data['score'],
            data['note']
        ))
        
        conn.commit()
        
        return jsonify({
            'message': 'Evaluation saved successfully',
            'url_video': data['url_video'],
            'criteria': data['criteria'],
            'score': data['score'],
            'note': data['note']
        }), 200

    except sqlite3.Error as e:
        print("Database error:", e)  # Debug log
        return jsonify({'error': f'Database error: {str(e)}'}), 500
    except Exception as e:
        print("General error:", e)  # Debug log
        return jsonify({'error': str(e)}), 500
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    print(f"Starting server...")
    print(f"Database location: {DB_PATH}")
    app.run(debug=True, use_reloader=False, port=3000)  # Disable only the reloader