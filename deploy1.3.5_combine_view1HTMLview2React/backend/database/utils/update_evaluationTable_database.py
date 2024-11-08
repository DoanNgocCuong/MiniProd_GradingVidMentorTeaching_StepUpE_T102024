import sqlite3
import os
from datetime import datetime

def insert_evaluation(url_video, criteria, score, note):
    # Get database path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, 'video_database.db')

    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Create evaluations table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS evaluations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                video_url TEXT,
                criteria TEXT,
                score INTEGER,
                note TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Insert evaluation record
        cursor.execute('''
            INSERT INTO evaluations (video_url, criteria, score, note, created_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (url_video, criteria, score, note, datetime.now().isoformat()))

        # Commit the changes
        conn.commit()
        print("Evaluation record inserted successfully!")

        # Verify the insertion
        cursor.execute('''
            SELECT * FROM evaluations 
            WHERE video_url = ? 
            AND criteria = ? 
            ORDER BY created_at DESC 
            LIMIT 1
        ''', (url_video, criteria))
        
        record = cursor.fetchone()
        if record:
            print("\nInserted record:")
            print(f"ID: {record[0]}")
            print(f"Video URL: {record[1]}")
            print(f"Criteria: {record[2]}")
            print(f"Score: {record[3]}")
            print(f"Note: {record[4]}")
            print(f"Timestamp: {record[5]}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Unexpected error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    # Example usage
    test_data = {
        "url_video": "https://drive.google.com/file/d/1ZDgW_R-vKmz3_A59y9UeicWXvWt2hoEL/view",
        "criteria": "Clarity",
        "score": 2,
        "note": "Clear and concise presentation"
    }
    
    insert_evaluation(
        test_data["url_video"],
        test_data["criteria"],
        test_data["score"],
        test_data["note"]
    )