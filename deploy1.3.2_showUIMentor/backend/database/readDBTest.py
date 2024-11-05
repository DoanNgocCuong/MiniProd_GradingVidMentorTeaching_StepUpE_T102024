
import sqlite3

import os
# Get correct database path - điều này để file có thể chạy ở bất kỳ vị trí nào của cửa sổ project, chỉ cần 2 file này cùng thư mục
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) # 
DB_PATH = os.path.join(CURRENT_DIR, 'video_database.db')

# Kết nối đến database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Truy vấn tất cả dữ liệu trong bảng
cursor.execute('SELECT * FROM video_transcripts')

# Lấy tất cả các dòng dữ liệu
rows = cursor.fetchall()

# In ra từng dòng dữ liệu
print("Tổng số bản ghi:", len(rows))
print("\nChi tiết các bản ghi:")
for row in rows:
    print("Row 0: \nID:", row[0])
    print("Row 1: Video URL:", row[1])
    print("Row 2: Transcription:", row[2])
    print("Created at:", row[3])
    print("Updated at:", row[4])
    print("Row 5: Criteria:", row[5])
    print("-" * 50)

# Đóng kết nối
conn.close()