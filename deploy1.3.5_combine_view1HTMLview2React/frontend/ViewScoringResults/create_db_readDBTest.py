import sqlite3
import os

# Lấy đường dẫn thư mục hiện tại
# - `__file__`: Đây là một biến đặc biệt trong Python chứa đường dẫn của file code hiện tại
# - `os.path.abspath()`: Chuyển đổi đường dẫn tương đối thành đường dẫn tuyệt đối (absolute path)
# - `os.path.dirname()`: Lấy tên thư mục chứa file (bỏ đi tên file)
# - Kết quả: `current_dir` sẽ chứa đường dẫn tuyệt đối đến thư mục chứa file code hiện tại

current_dir = os.path.dirname(os.path.abspath(__file__))  
# db_path = os.path.join(current_dir, 'video_database.db')  # Đường dẫn cũ để kết nối với cơ sở dữ liệu video_database.db
# Lấy đường dẫn thư mục cha, đi lên một cấp để vào thư mục backend
parent_dir = os.path.dirname(current_dir)  # Go up one level to backend folder
# Tạo đường dẫn mới đến cơ sở dữ liệu video_database.db trong thư mục database
db_path = os.path.join(parent_dir, 'database', 'video_database.db')

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

    # Print results
    print(f"\nTotal records: {len(rows)}")
    print("\nRecord details:")
    
    for row in rows:
        print("\n" + "="*50)
        print(f"ID: {row[0]}")
        print(f"Video URL: {row[1]}")
        print(f"Transcription: {row[2][:150]}...")  # Preview first 100 chars
        print(f"Criteria: {row[3]}...")       # Preview first 100 chars
        print(f"Created at: {row[4]}")

except sqlite3.OperationalError as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    conn.close()