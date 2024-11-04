
import sqlite3

# Kết nối đến database
conn = sqlite3.connect('video_database.db')
cursor = conn.cursor()

# Truy vấn tất cả dữ liệu trong bảng
cursor.execute('SELECT * FROM video_transcripts')

# Lấy tất cả các dòng dữ liệu
rows = cursor.fetchall()

# In ra từng dòng dữ liệu
print("Tổng số bản ghi:", len(rows))
print("\nChi tiết các bản ghi:")
for row in rows:
    print("\nID:", row[0])
    print("Video URL:", row[1])
    print("Transcription:", row[2])
    print("Created at:", row[3])
    print("Updated at:", row[4])
    print("-" * 50)

# Đóng kết nối
conn.close()