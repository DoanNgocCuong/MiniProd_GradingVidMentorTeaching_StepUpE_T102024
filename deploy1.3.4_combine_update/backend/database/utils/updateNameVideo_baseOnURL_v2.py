import sqlite3
import os
from urllib.parse import urlparse, parse_qs

def extract_filename_from_url(url):
    # Parse the URL
    parsed = urlparse(url)
    # Get the path component
    path = parsed.path
    # Split the path and get the file ID
    file_id = path.split('/')[-2]
    return file_id

def update_database():
    # Get database path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    db_path = os.path.join(parent_dir, 'video_database.db')

    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Check if the column already exists
        cursor.execute("PRAGMA table_info(videos)")
        columns = [column[1] for column in cursor.fetchall()]
        if 'name_video' not in columns:
            # Add new column
            cursor.execute('''ALTER TABLE videos ADD COLUMN name_video TEXT''')

        # Fetch all video URLs
        cursor.execute('SELECT id, url_video FROM videos')
        rows = cursor.fetchall()
        
        # Update name_video for each row based on the video ID mapping
        video_names = {
            '10qe6DkNX6up7-oG69HRG3B4j1A-WiI_o': 'Bản sao của 0973453282 - 09/10 - B6',
            '1wU7VG6RoQSIT4Nx3nzre3c9kf8IP3vPs': 'Bản sao của 0383521988 - 08/10 - B28',
            '1cTQEfu1ftdHcHA42oDt4EphgjMI2yStD': 'Bản sao của 0912338926 - 09/10 - B10',
            '1Bjc2DjRMKCg7-aTV7x4g8qGtBVcDxMT_': 'Bản sao của 0398678257 - 09/10 - B2',
            '1x31CUa503coR26Tl-DIgMxiJaJmAWPmF': 'Bản sao của 0961797200 - 09/10 - B13',
            '172JnO5uHq-ijmanNhDqZJtQQFZ2H3QN2': 'Bản sao của 0989741503 - 10/10 - B12',
            '1Xj4nOZEf8-lWpub6AOSClmV81NOhkfRl': 'Bản sao của 0377642151 - 09/10 - B16',
            '1oovK9faTksePgr5RF5H_UegY9VA1800D': 'Bản sao của 0949911296 - 09/10 - B16',
            '1qetq0udB096mOpue8XyHtaUUYudB0k_Y': 'Bản sao của 0898347747 - 10/10 - B5',
            '1ZDgW_R-vKmz3_A59y9UeicWXvWt2hoEL': 'Bản sao của 0345100005 - 09/10 - B17'
        }
        
        for row_id, url in rows:
            file_id = extract_filename_from_url(url)
            name = video_names.get(file_id, 'Unknown')
            cursor.execute('''
                UPDATE videos 
                SET name_video = ? 
                WHERE id = ?
            ''', (name, row_id))

        # Commit the changes
        conn.commit()
        print("Database updated successfully!")
        
        # Verify the update
        cursor.execute('SELECT id, name_video, url_video FROM videos')
        updated_rows = cursor.fetchall()
        print("\nUpdated records:")
        for row in updated_rows:
            print(f"ID: {row[0]}, Name: {row[1][:100]}")

        # Print full table
        cursor.execute('SELECT * FROM videos')
        full_table_rows = cursor.fetchall()
        print("\nFull table records:")
        for row in full_table_rows:
            # Cắt mỗi trường tối đa 100 ký tự
            truncated_row = [str(field)[:100] for field in row]
            print(truncated_row)  # In ra danh sách các trường đã cắt

    except sqlite3.OperationalError as e:
        print(f"Database error: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Unexpected error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    update_database()