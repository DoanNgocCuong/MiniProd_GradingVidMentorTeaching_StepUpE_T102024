import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import requests
import json
import re
import logging
import sqlite3
import io

# Set up logging
logging.basicConfig(level=logging.INFO)

url = 'http://103.253.20.13:25029/role_assign'
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

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
            transcript TEXT,
            raw_whisper_output TEXT
        )
    ''')
    conn.commit()
    conn.close()

def update_or_insert_data(file_name_video, file_name_audio, url_video, url_audio, transcript, raw_whisper_output="", id=None):
    try:
        with sqlite3.connect('audio_data.db') as conn:
            c = conn.cursor()
            if id is not None:
                # Check if ID exists
                c.execute('SELECT COUNT(*) FROM audio_data WHERE id = ?', (id,))
                exists = c.fetchone()[0] > 0
                
                if exists:
                    # Update existing record
                    c.execute('''
                        UPDATE audio_data 
                        SET file_name_video=?, file_name_audio=?, url_video=?, url_audio=?, transcript=?, raw_whisper_output=?
                        WHERE id=?
                    ''', (file_name_video, file_name_audio, url_video, url_audio, transcript, raw_whisper_output, id))
                    print(f"Updated record with ID: {id}")
                else:
                    # Insert new record
                    c.execute('''
                        INSERT INTO audio_data (id, file_name_video, file_name_audio, url_video, url_audio, transcript, raw_whisper_output)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (id, file_name_video, file_name_audio, url_video, url_audio, transcript, raw_whisper_output))
                    print(f"Inserted new record with ID: {id}")
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error with database operation: {e}")

def process_audio_from_url(url, language='en'):
    """Process audio directly from URL"""
    try:
        # Download audio content
        response = requests.get(url)
        response.raise_for_status()
        audio_content = response.content

        # Prepare for Whisper API
        files = {'audio': ('audio', audio_content)}
        data = {
            'secret_key': 'codedongian',
            'language': language
        }

        # Send to Whisper API
        whisper_response = requests.post(url, files=files, data=data)
        whisper_response.raise_for_status()
        
        return whisper_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error processing audio: {e}")
        return None

def combine_transcripts(mentor_output, hv_output):
    """Combine mentor and HV transcripts"""
    try:
        # Parse outputs
        mentor_data = json.loads(mentor_output['raw_whisper_output']) if isinstance(mentor_output['raw_whisper_output'], str) else mentor_output['raw_whisper_output']
        hv_data = json.loads(hv_output['raw_whisper_output']) if isinstance(hv_output['raw_whisper_output'], str) else hv_output['raw_whisper_output']

        # Extract and format timestamps
        combined_data = []
        
        # Add mentor data
        for item in mentor_data:
            timestamp = item.get('start_time', 0)
            combined_data.append({
                'time': timestamp,
                'speaker': 'Mentor',
                'text': item.get('text', '')
            })
            
        # Add HV data
        for item in hv_data:
            timestamp = item.get('start_time', 0)
            combined_data.append({
                'time': timestamp,
                'speaker': 'HV',
                'text': item.get('text', '')
            })
            
        # Sort by timestamp
        combined_data.sort(key=lambda x: x['time'])
        
        # Format into readable transcript
        formatted_transcript = []
        for item in combined_data:
            minutes = int(item['time'] / 60000)
            seconds = int((item['time'] % 60000) / 1000)
            timestamp = f"[{minutes:02d}:{seconds:02d}]"
            formatted_transcript.append(f"{timestamp} {item['speaker']}: {item['text']}")
            
        return "\n".join(formatted_transcript)
    except Exception as e:
        print(f"Error combining transcripts: {e}")
        return None

def process_drive_folder(folder_id):
    """Process Google Drive folder"""
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
    
    try:
        # Get all files in folder
        query = f"'{folder_id}' in parents"
        results = service.files().list(q=query, fields="files(id, name, mimeType)").execute()
        items = results.get('files', [])

        current_id = 1
        mentor_outputs = {}
        hv_outputs = {}

        for item in items:
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                if item['name'] == 'Audio':
                    # Process Audio folder
                    audio_query = f"'{item['id']}' in parents"
                    audio_files = service.files().list(q=audio_query, fields="files(id, name)").execute().get('files', [])
                    
                    for audio_file in audio_files:
                        url = f'https://drive.google.com/uc?id={audio_file["id"]}'
                        
                        # Process audio with Whisper API
                        output = process_audio_from_url(url)
                        if output:
                            if 'mentor' in audio_file['name'].lower():
                                mentor_outputs[audio_file['name']] = {
                                    'raw_whisper_output': json.dumps(output),
                                    'url': url
                                }
                            elif 'hv' in audio_file['name'].lower():
                                hv_outputs[audio_file['name']] = {
                                    'raw_whisper_output': json.dumps(output),
                                    'url': url
                                }
                            
                            # Save raw output to database
                            update_or_insert_data(
                                file_name_video='',
                                file_name_audio=audio_file['name'],
                                url_video='',
                                url_audio=url,
                                transcript='',
                                raw_whisper_output=json.dumps(output),
                                id=current_id
                            )
                            current_id += 1

                elif item['name'] == 'Video':
                    # Process Video folder
                    video_query = f"'{item['id']}' in parents"
                    video_files = service.files().list(q=video_query, fields="files(id, name)").execute().get('files', [])
                    
                    for video_file in video_files:
                        url = f'https://drive.google.com/uc?id={video_file["id"]}'
                        update_or_insert_data(
                            file_name_video=video_file['name'],
                            file_name_audio='',
                            url_video=url,
                            url_audio='',
                            transcript='',
                            id=current_id
                        )
                        current_id += 1

        # Combine mentor and HV transcripts
        for mentor_name, mentor_data in mentor_outputs.items():
            base_name = mentor_name.replace('mentor', '').strip()
            hv_name = next((name for name in hv_outputs if base_name in name), None)
            
            if hv_name:
                combined_transcript = combine_transcripts(mentor_data, hv_outputs[hv_name])
                if combined_transcript:
                    update_or_insert_data(
                        file_name_video='',
                        file_name_audio=f"{base_name}_combined",
                        url_video='',
                        url_audio='',
                        transcript=combined_transcript,
                        id=current_id
                    )
                    current_id += 1

    except Exception as e:
        print(f"Error processing Drive folder: {e}")

def fetch_data(max_chars=100):
    """Fetch and display data from database"""
    conn = sqlite3.connect('audio_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM audio_data')
    rows = c.fetchall()

    for row in rows:
        transcript_preview = row[5][:max_chars] 
        if row[5] and len(row[5]) > max_chars:
            transcript_preview += '...'
        print(f"ID: {row[0]}, FILE NAME VIDEO: {row[1]}, FILE NAME AUDIO: {row[2]}, URL VIDEO: {row[3]}, URL AUDIO: {row[4]}, TRANSCRIPT: {transcript_preview}")

    conn.close()

if __name__ == '__main__':
    create_database()
    process_drive_folder("1_oVkhMaU4M1-ZIkb5sL4XSRE1LmZUn3z")
    print("\nDatabase contents:")
    fetch_data()