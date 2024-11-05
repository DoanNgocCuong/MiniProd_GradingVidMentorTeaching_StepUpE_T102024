import sqlite3

# View DB
def fetch_data(max_chars=10):
    """
    Fetch and display data from the audio_data database table.

    This function connects to the SQLite database, retrieves all rows from the audio_data table,
    and prints a formatted summary of each row. The transcript field is truncated to a specified
    maximum number of characters for brevity.

    Parameters:
    max_chars (int): The maximum number of characters to display for the transcript preview.
                     If the transcript is longer, it will be truncated and ellipsis (...) will be added.
                     Default is 10 characters.

    Returns:
    None: This function doesn't return any value, it prints the data to the console.
    """
    conn = sqlite3.connect('audio_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM audio_data')
    rows = c.fetchall()

    for row in rows:
        transcript_preview = row[5][:max_chars] 
        if len(row[5]) > max_chars:
            transcript_preview += '...'
        print(f"ID: {row[0]}, FILE NAME VIDEO: {row[1]}, FILE NAME AUDIO: {row[2]}, URL VIDEO: {row[3]}, URL AUDIO: {row[4]}, TRANSCRIPT: {transcript_preview}")

    conn.close()



if __name__ == '__main__':
    # Fetch and display data
    fetch_data()
