import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import gdown

# Whisper
import requests
import os
import json
import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# DB
import sqlite3
import time

url = 'http://103.253.20.13:25029/role_assign'

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


# Function to create the database and the table
def create_database():
    conn = sqlite3.connect('audio_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS audio_data (
            id INTEGER PRIMARY KEY,
            file_name_video TEXT,
            file_name_audio TEXT,
            url_video TEXT,  
            url_audio TEXT,
            transcript TEXT
        )
    ''')
    conn.commit()
    conn.close()


def insert_data(file_name_video, file_name_audio, url_video, url_audio, transcript, id=None):
    try:
        with sqlite3.connect('audio_data.db') as conn:
            c = conn.cursor()
            if id is not None:
                c.execute('''
                    INSERT INTO audio_data (id, file_name_video, file_name_audio, url_video, url_audio, transcript)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (id, file_name_video, file_name_audio, url_video, url_audio, transcript))
            else:
                c.execute('''
                    INSERT INTO audio_data (file_name_video, file_name_audio, url_video, url_audio, transcript)
                    VALUES (?, ?, ?, ?, ?)
                ''', (file_name_video, file_name_audio, url_video, url_audio, transcript))
            conn.commit()
    except sqlite3.IntegrityError:
        print("Error: ID already exists.")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")


def extract_dicts(s):
    """Extract dictionaries from a string containing JSON objects."""
    pattern = r"\{[^{}]*\}"
    matches = re.findall(pattern, s)
    result = []
    
    for match in matches:
        try:
            match = match.replace("'", '"')
            d = json.loads(match)
            result.append(d)
        except json.JSONDecodeError:
            # logging.warning(f"Error decoding JSON: {match}")
            pass
    
    return result

def format_time(milliseconds):
    """Format milliseconds into a readable time string."""
    seconds = milliseconds // 1000
    minutes = seconds // 60
    hours = minutes // 60
    return f"{hours:02d}:{minutes%60:02d}:{seconds%60:02d}"


def process_audio(audio_path, language):
    
    with open(audio_path, 'rb') as audio_file:
        files = {'audio': audio_file}
        data = {
            'secret_key': 'codedongian',
            'language': language
        }

        response = requests.post(url, files=files, data=data)

        if response.status_code == 200:
            output = response.json()
            return output
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None


def process_audio_outputs(output1, output2, output_filename):
    if output1 and output2:
        output1_data = extract_dicts(output1['output'])
        output2_data = extract_dicts(output2['output'])

        for item in output1_data:
            item['speaker'] = '1'

        for item in output2_data:
            item['speaker'] = '2'

        combined_output = sorted(output1_data + output2_data, key=lambda x: x['start_time'])

        formatted_output = []
        for item in combined_output:
            formatted_time = format_time(item['start_time'])
            formatted_output.append(f"[{formatted_time}] Speaker {item['speaker']}: {item['text']}")

        # Convert the formatted_output list to a single string
        formatted_transcript = "\n".join(formatted_output)

        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write("\n".join(formatted_output))

        print(f"Output has been saved to {output_filename}")
        print("\n")
    else:
        print("Error processing audio files. Please check the file paths and try again.")
    
    return formatted_transcript


def google_drive_files():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    folder_id = '1_oVkhMaU4M1-ZIkb5sL4XSRE1LmZUn3z'

    # Get folder metadata
    folder = service.files().get(fileId=folder_id, fields="name").execute()
    folder_name = folder.get('name', 'Unknown Folder')

    # Create local directories
    local_parent_folder = os.path.join('audio_data', folder_name)
    os.makedirs(local_parent_folder, exist_ok=True)

    local_text_folder = os.path.join(local_parent_folder, 'Text')
    os.makedirs(local_text_folder, exist_ok=True)

    # Get all files and folders in the main folder
    query = f"'{folder_id}' in parents"
    results = service.files().list(q=query, fields="files(id, name, mimeType)").execute()
    items = results.get('files', [])

    print(f'Files in folder: {folder_name}')

    # Initialize ID variable
    current_id = 1

    # Store video filenames for later use
    video_files_dict = {}

    for item in items:
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            if item['name'] == 'Video':
                video_folder_id = item['id']
                video_query = f"'{video_folder_id}' in parents"
                video_files = service.files().list(q=video_query, fields="files(id, name)").execute().get('files', [])

                print(f'\nVideo Files:')
                if not video_files:
                    print('  No video files found.')
                else:
                    for video_file in video_files:
                        file_url = f"https://drive.google.com/file/d/{video_file['id']}/view"
                        print(f"  {video_file['name']}: {file_url}")
                        url = f'https://drive.google.com/uc?id={video_file["id"]}'
                        video_files_dict[video_file['name']] = {
                            'id': video_file['id'],
                            'url': url
                        }

                        # Insert video data using the current ID
                        insert_data(video_file['name'], '', url, '', '', id=current_id)

                        # Increment the ID for the next loop iteration
                        current_id += 1

            elif item['name'] == 'Audio':
                audio_folder_id = item['id']
                audio_query = f"'{audio_folder_id}' in parents"
                audio_files = service.files().list(q=audio_query, fields="files(id, name)").execute().get('files', [])

                local_audio_folder = os.path.join(local_parent_folder, 'Audio')
                os.makedirs(local_audio_folder, exist_ok=True)

                print(f'\nAudio Files:')
                if not audio_files:
                    print('  No audio files found.')
                else:
                    for audio_file in audio_files:
                        file_url = f"https://drive.google.com/file/d/{audio_file['id']}/view"
                        print(f"  {audio_file['name']}: {file_url}")

                        # Download files from Audio folder
                        url = f'https://drive.google.com/uc?id={audio_file["id"]}'
                        local_audio_file_path = os.path.join(local_audio_folder, audio_file['name'])
                        gdown.download(url, local_audio_file_path, quiet=False)
                        time.sleep(3)

                        # Process the downloaded audio file
                        output = process_audio(local_audio_file_path, 'en')
                        if output:
                            output_filename = os.path.splitext(audio_file['name'])[0] + '.txt'
                            output_file_path = os.path.join(local_text_folder, output_filename)
                            with open(output_file_path, 'w', encoding='utf-8') as f:
                                json.dump(output, f, ensure_ascii=False, indent=2)
                            print(f"Output saved to: {output_file_path}")
                            print("\n")

                        # Insert audio data using the current ID
                        insert_data('', audio_file['name'], '', url, '', id=current_id)

                        # Increment the ID for the next loop iteration
                        current_id += 1

                        # Check for the presence of HV.txt and mentor.txt files
                        has_hv = any(filename.endswith('HV.txt') for filename in os.listdir(local_text_folder))
                        has_mentor = any(filename.endswith('mentor.txt') for filename in os.listdir(local_text_folder))

                        if has_hv and has_mentor:
                            transcript_folder = os.path.join(local_parent_folder, 'Transcript')
                            os.makedirs(transcript_folder, exist_ok=True)

                            for filename in os.listdir(local_text_folder):
                                if filename.endswith('HV.txt'):
                                    hv_file = os.path.join(local_text_folder, filename)
                                    mentor_file = hv_file.replace('HV.txt', 'mentor.txt')

                                    if os.path.isfile(mentor_file):
                                        with open(hv_file, 'r', encoding='utf-8') as f:
                                            output1 = {'output': f.read()}

                                        with open(mentor_file, 'r', encoding='utf-8') as f:
                                            output2 = {'output': f.read()}

                                        # New filename derived from the HV.txt
                                        new_filename = os.path.join(transcript_folder, filename.replace(' - HV.txt', '.txt'))
                                        output = process_audio_outputs(output1, output2, new_filename)

                                        # Extract video name from the new_filename 
                                        base_filename = os.path.basename(new_filename)  
                                        video_filename = base_filename.replace('.txt', '.mp4')  

                                        # Find the matching video file in the dictionary
                                        if video_filename in video_files_dict:
                                            video_data = video_files_dict[video_filename]
                                            video_url = video_data['url']

                                            # Insert the processed transcript (output) into the database for the corresponding video entry
                                            insert_data(video_filename, '', video_url, '', output, id=current_id)

                                            print(f"Output saved to video entry: {video_filename}")

                                            # Increment the ID for the next loop iteration
                                            current_id += 1

                                        os.remove(hv_file)
                                        os.remove(mentor_file)
                                        print(f"Deleted {hv_file} and {mentor_file} from {local_text_folder}.")
                                    else:
                                        print(f"Corresponding mentor file not found for {filename}.")

    return None


# View DB
def fetch_data(max_chars=10):
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


def insert_video_audio_data(id, file_name_video, url_video, file_name_audio, url_audio):
    try:
        with sqlite3.connect('audio_data.db') as conn:
            c = conn.cursor()

            # Check if an entry with the same ID already exists (to avoid duplicate entries)
            c.execute('SELECT id FROM audio_data WHERE id = ?', (id,))
            if c.fetchone():
                print(f"ID {id} already exists in the database. Skipping insert.")
                return

            # Insert video and audio data into the database for the given ID
            c.execute('''
                INSERT INTO audio_data (id, file_name_video, url_video, file_name_audio, url_audio)
                VALUES (?, ?, ?, ?, ?)
            ''', (id, file_name_video, url_video, file_name_audio, url_audio))

            conn.commit()
            print(f"Data inserted for ID {id}: Video - {file_name_video}, Audio - {file_name_audio}")

    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

def fetch_data_by_url(url):
    try:
        # Connect to the database
        with sqlite3.connect('audio_data.db') as conn:
            c = conn.cursor()
            # Query to select all columns where the URL matches
            c.execute('''
                SELECT * FROM audio_data
                WHERE url_video = ? OR url_audio = ?
            ''', (url, url))
            
            # Fetch all matching rows
            rows = c.fetchall()
        
        return rows
    
    except sqlite3.Error as e:
        print(f"Error fetching data: {e}")
        return []


if __name__ == '__main__':
    create_database()

    google_drive_files()

    print("\n\n")

    # Fetch and display data
    fetch_data()

    # Insert manually
    # insert_video_audio_data(id, file_name_video, url_video, file_name_audio, url_audio)

    # url_to_search = 'https://drive.google.com/uc?id=1qTR8xJLhA2eItsWgpyxzjnV1zNni6H3m'
    # matching_rows = fetch_data_by_url(url_to_search)
