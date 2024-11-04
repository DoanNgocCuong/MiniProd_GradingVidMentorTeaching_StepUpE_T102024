import sqlite3

def fetch_all_data():
    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect('audio_data.db')  # Thay thế bằng tên tệp cơ sở dữ liệu của bạn
    cursor = conn.cursor()

    # Thực hiện câu lệnh SELECT để lấy toàn bộ dữ liệu
    cursor.execute('SELECT * FROM audio_data')  # Thay thế bằng tên bảng của bạn

    # Lấy tất cả các kết quả
    rows = cursor.fetchall()

    # In ra các kết quả
    for row in rows:
        print(f"ID: {row[0]}, FILE NAME VIDEO: {row[1]}, FILE NAME AUDIO: {row[2]}, URL VIDEO: {row[3]}, URL AUDIO: {row[4]}, TRANSCRIPT: {row[5]}")

    # Đóng kết nối
    conn.close()

# Gọi hàm để lấy và hiển thị dữ liệu
fetch_all_data()