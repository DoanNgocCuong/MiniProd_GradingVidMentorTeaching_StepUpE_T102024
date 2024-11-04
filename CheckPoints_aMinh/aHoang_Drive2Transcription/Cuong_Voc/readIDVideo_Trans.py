import sqlite3

def get_video_transcripts():
    """
    Lấy tất cả url_video và transcript từ database
    Returns: list of tuples (url_video, transcript)
    """
    try:
        with sqlite3.connect('audio_data.db') as conn:
            c = conn.cursor()
            c.execute('SELECT url_video, transcript FROM audio_data WHERE url_video != ""')
            results = c.fetchall()
            return results
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

def get_video_transcript_by_name(video_name):
    """
    Lấy url_video và transcript của một video cụ thể
    Args:
        video_name: tên file video
    Returns: tuple (url_video, transcript)
    """
    try:
        with sqlite3.connect('audio_data.db') as conn:
            c = conn.cursor()
            c.execute('SELECT url_video, transcript FROM audio_data WHERE file_name_video = ?', (video_name,))
            result = c.fetchone()
            return result
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

def get_all_video_data():
    """
    Lấy toàn bộ thông tin liên quan đến video
    Returns: list of dicts với thông tin đầy đủ
    """
    try:
        with sqlite3.connect('audio_data.db') as conn:
            c = conn.cursor()
            c.execute('''
                SELECT 
                    file_name_video,
                    url_video,
                    transcript
                FROM audio_data 
                WHERE url_video != ""
                ORDER BY file_name_video
            ''')
            columns = ['file_name', 'url', 'transcript']
            results = [dict(zip(columns, row)) for row in c.fetchall()]
            return results
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

# Example usage:
if __name__ == "__main__":
    # Lấy tất cả video và transcript
    print("\nAll video transcripts:")
    all_videos = get_video_transcripts()
    for url, transcript in all_videos:
        print(f"URL: {url}")
        print(f"Transcript preview: {transcript[:100]}...\n")

    # Lấy theo tên video cụ thể
    video_name = "0345100005 - 09_10 - B17.mp4"
    print(f"\nLooking for video: {video_name}")
    video_data = get_video_transcript_by_name(video_name)
    if video_data:
        url, transcript = video_data
        print(f"URL: {url}")
        print(f"Transcript preview: {transcript[:100]}...\n")
    else:
        print("Video not found")

    # Lấy thông tin đầy đủ
    print("\nFull video information:")
    video_data = get_all_video_data()
    for video in video_data:
        print(f"File name: {video['file_name']}")
        print(f"URL: {video['url']}")
        print(f"Transcript preview: {video['transcript'][:100]}...\n")