import sqlite3
import json

def get_video_info(video_url):
    """
    Trích xuất thông tin video từ database dựa vào URL
    """
    try:
        # Kết nối database
        conn = sqlite3.connect('video_database.db')
        cursor = conn.cursor()

        # Truy vấn thông tin
        cursor.execute('''
            SELECT video_url, transcription, criteria
            FROM video_transcripts 
            WHERE video_url = ?
        ''', (video_url,))
        
        result = cursor.fetchone()
        
        if result:
            video_info = {
                "video_url": result[0],
                "transcription": result[1],
                "criteria": json.loads(result[2]) if result[2] else None
            }
            
            print("\nThông tin video:")
            print("-" * 50)
            print("URL:", video_info["video_url"])
            print("\nTranscription:", video_info["transcription"][:200] + "..." 
                  if len(video_info["transcription"]) > 200 else video_info["transcription"])
            print("\nCriteria:", json.dumps(video_info["criteria"], indent=2, ensure_ascii=False) 
                  if video_info["criteria"] else "Chưa có criteria")
            
            return video_info
        else:
            print("Không tìm thấy thông tin cho URL này")
            return None

    except sqlite3.Error as e:
        print("Lỗi database:", str(e))
        return None
    except json.JSONDecodeError as e:
        print("Lỗi khi đọc JSON criteria:", str(e))
        return None
    except Exception as e:
        print("Lỗi không xác định:", str(e))
        return None
    finally:
        conn.close()

if __name__ == "__main__":
    # URL video cần trích xuất thông tin
    url_video = "https://drive.google.com/file/d/10qe6DkNX6up7-oG69HRG3B4j1A-WiI_o/view"
    
    video_info = get_video_info(url_video)