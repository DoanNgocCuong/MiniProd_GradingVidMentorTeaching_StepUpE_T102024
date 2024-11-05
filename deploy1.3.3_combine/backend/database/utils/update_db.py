import sqlite3

# URL video cần update
url_video = "https://drive.google.com/file/d/10qe6DkNX6up7-oG69HRG3B4j1A-WiI_o/view"
new_transcription = """[00:00:00] Speaker 1: Okay, so the day before, we solved that problem together.
[00:00:07] Speaker 1: We... Alright, how do I say?
[00:00:10] Speaker 1: We expanded ideas for the Vietnam Food Contest, right?
# ... phần transcription tiếp theo ...
[00:29:08] Speaker 1: See you.
[00:29:09] Speaker 1: Bye-bye."""

# Kết nối đến database
conn = sqlite3.connect('video_database.db')
cursor = conn.cursor()

# Kiểm tra xem URL đã tồn tại chưa
cursor.execute('SELECT id FROM video_transcripts WHERE video_url = ?', (url_video,))
result = cursor.fetchone()

if result:
    # Nếu URL đã tồn tại, update transcription
    cursor.execute('''
        UPDATE video_transcripts 
        SET transcription = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE video_url = ?
    ''', (new_transcription, url_video))
    print("Đã cập nhật transcription cho URL hiện có")
else:
    # Nếu URL chưa tồn tại, insert mới
    cursor.execute('''
        INSERT INTO video_transcripts (video_url, transcription)
        VALUES (?, ?)
    ''', (url_video, new_transcription))
    print("Đã thêm mới URL và transcription")

# Lưu thay đổi
conn.commit()

# Kiểm tra kết quả
cursor.execute('SELECT id, video_url, transcription, created_at, updated_at FROM video_transcripts WHERE video_url = ?', (url_video,))
result = cursor.fetchone()
if result:
    print("\nThông tin sau khi cập nhật:")
    print("ID:", result[0])
    print("URL:", result[1]) 
    print("Transcription:", result[2])
    print("Created at:", result[3])
    print("Updated at:", result[4])

# Đóng kết nối
conn.close()