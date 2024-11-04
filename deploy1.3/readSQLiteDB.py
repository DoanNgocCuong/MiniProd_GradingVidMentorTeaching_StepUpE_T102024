import sqlite3

# Kết nối đến file .db
conn = sqlite3.connect('CheckPoints_aMinh/aHoang_Drive2Transcription/audio_data.db')

# Tạo một con trỏ
cursor = conn.cursor()

# Lấy danh sách các bảng trong cơ sở dữ liệu
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# In ra tên các bảng
for table in tables:
    print(table[0])

# Đóng kết nối
conn.close()