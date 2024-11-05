import sqlite3
import requests
import json
import os

# URL video cụ thể
url_video = "https://drive.google.com/file/d/10qe6DkNX6up7-oG69HRG3B4j1A-WiI_o/view"

# Get correct database path - điều này để file có thể chạy ở bất kỳ vị trí nào của cửa sổ project, chỉ cần 2 file này cùng thư mục
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) # 
DB_PATH = os.path.join(CURRENT_DIR, 'video_database.db')

# Kết nối đến database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

try:
    # Thêm column criteria nếu chưa tồn tại
    cursor.execute('''
        SELECT COUNT(*) FROM pragma_table_info('video_transcripts') 
        WHERE name='criteria'
    ''')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            ALTER TABLE video_transcripts
            ADD COLUMN criteria TEXT
        ''')
        print("Đã thêm cột criteria vào database")

    # Lấy transcription từ database
    cursor.execute('SELECT transcription FROM video_transcripts WHERE video_url = ?', (url_video,))
    result = cursor.fetchone()

    if result:
        transcription = result[0]
        
        # Gửi request đến API
        api_url = 'http://localhost:5000/analyze'
        headers = {'Content-Type': 'application/json'}
        data = {"transcription": transcription}
        
        try:
            response = requests.post(api_url, headers=headers, json=data)
            
            # Kiểm tra status code
            response.raise_for_status()
            
            criteria_json = response.json()
            
            # Lưu kết quả JSON vào database
            cursor.execute('''
                UPDATE video_transcripts 
                SET criteria = ?,
                    updated_at = CURRENT_TIMESTAMP
                WHERE video_url = ?
            ''', (json.dumps(criteria_json), url_video))
            
            conn.commit()
            print("\nĐã cập nhật criteria thành công!")
            
            # Kiểm tra kết quả
            cursor.execute('''
                SELECT id, video_url, transcription, criteria, created_at, updated_at 
                FROM video_transcripts 
                WHERE video_url = ?
            ''', (url_video,))
            updated_result = cursor.fetchone()
            
            if updated_result:
                print("\nThông tin sau khi cập nhật:")
                print("ID:", updated_result[0])
                print("URL:", updated_result[1])
                print("\nTranscription:", updated_result[2][:200] + "...") # Chỉ hiển thị 200 ký tự đầu
                print("\nCriteria:", json.loads(updated_result[3]))
                print("\nCreated at:", updated_result[4])
                print("Updated at:", updated_result[5])
                
        except requests.exceptions.RequestException as e:
            print("Lỗi khi gọi API:", str(e))
        except json.JSONDecodeError as e:
            print("Lỗi khi xử lý JSON:", str(e))
        except Exception as e:
            print("Lỗi không xác định:", str(e))
    else:
        print("Không tìm thấy transcription cho URL này")

except sqlite3.Error as e:
    print("Lỗi database:", str(e))
    
finally:
    # Đóng kết nối
    conn.close()