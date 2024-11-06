# backend/database/api_database_app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

# Get correct database path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) # 
DB_PATH = os.path.join(CURRENT_DIR, 'database/video_database_1.db')

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
        
        # Kết nối database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Thêm bảng evaluations nếu chưa tồn tại
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS evaluations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                video_url TEXT,
                criteria TEXT,
                score INTEGER,
                feedback TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Insert dữ liệu đánh giá
        cursor.execute('''
            INSERT INTO evaluations (video_url, criteria, score, feedback)
            VALUES (?, ?, ?, ?)
        ''', (data['videoUrl'], data['criteria'], data['score'], data['feedback']))
        
        conn.commit()
        
        return jsonify({'message': 'Evaluation saved successfully'}), 200

    except Exception as e:
        print(f"Error saving evaluation: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    print(f"Starting server...")
    print(f"Database location: {DB_PATH}")
    app.run(debug=True, port=3000)