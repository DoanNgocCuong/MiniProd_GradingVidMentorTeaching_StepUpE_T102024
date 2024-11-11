import sqlite3
import os

# Get database path
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'video_database.db')

# Connect to database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    # Show all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("Tables in database:", cursor.fetchall())
    
    # Query videos table
    cursor.execute('SELECT * FROM videos')   # tên bảng là videos đã tạo từ workflow.py
    rows = cursor.fetchall()

    # Print results and write to file
    print(f"\nTotal records: {len(rows)}")
    print("\nRecord details:")
    
    with open('testReadDB.txt', 'w', encoding='utf-8') as f:
        f.write(f"Total records: {len(rows)}\n\nRecord details:\n")
        for row in rows:
            separator = "="*50
            f.write(f"\n{separator}\n")
            f.write(f"ID: {row[0]}\n")
            f.write(f"Video URL: {row[1]}\n")
            f.write(f"Transcription: {row[2][:150]}...\n")
            f.write(f"Criteria: {row[3]}...\n")
            f.write(f"Created at: {row[4]}\n")
            
            # Also print to console
            print("\n" + separator)
            print(f"ID: {row[0]}")
            print(f"Video URL: {row[1]}")
            print(f"Transcription: {row[2][:150]}")
            print(f"Criteria: {row[3]}...")
            print(f"Created at: {row[4]}")

except sqlite3.OperationalError as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    conn.close()