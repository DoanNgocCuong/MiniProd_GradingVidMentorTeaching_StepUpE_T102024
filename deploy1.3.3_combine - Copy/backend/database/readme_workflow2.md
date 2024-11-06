# Video Processing Workflow

A Python script for processing videos from Google Drive, extracting transcriptions, and analyzing criteria. This workflow automates the process of handling video files, generating transcriptions, and storing results in a SQLite database.

## Features

- Google Drive integration for video file access
- Audio transcription using speech-to-text API
- Transcript analysis for criteria generation
- SQLite database storage
- Temporary file management with auto-cleanup
- Comprehensive error handling and logging

## Prerequisites

### Required Python Version
- Python 3.7 or higher

### Required API Keys & Credentials
- Google Drive API credentials (`credentials.json`)
- Speech-to-text API secret key

### Dependencies
```bash
pip install google-auth google-auth-oauthlib google-api-python-client gdown requests
```

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd video-workflow
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up Google Drive credentials:
- Place your `credentials.json` file in the project root directory
- On first run, the script will prompt you to authenticate with Google

## File Structure

```
video-workflow/
├── workflow.py          # Main script
├── credentials.json     # Google Drive API credentials
├── videos.db           # SQLite database
├── temp_videos/        # Temporary storage for processing
└── logs/              # Log files
```

## Database Schema

```sql
CREATE TABLE videos (
    id INTEGER PRIMARY KEY,
    url_video TEXT NOT NULL,
    transcription TEXT,
    criteria TEXT,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## API Endpoints

### Transcription API
- URL: `http://103.253.20.13:25029/role_assign`
- Method: POST
- Parameters:
  - `audio`: Audio file
  - `secret_key`: Authentication key
  - `language`: Language code (e.g., 'en')

### Analysis API
- URL: `http://103.253.20.13:25034/analyze`
- Method: POST
- Headers: `Content-Type: application/json`
- Body:
  ```json
  {
    "transcription": "transcription_text"
  }
  ```

## Usage

1. Configure settings in the script:
```python
class Config:
    TEMP_FILE_TTL = timedelta(hours=24)  # Adjust temporary file lifetime
    # ... other settings
```

2. Run the script:
```bash
python workflow.py
```

3. Process specific folder:
```python
folder_id = "your_folder_id"  # Replace with your Google Drive folder ID
processor.process_folder(folder_id)
```

## Workflow Process

1. **Authentication**
   - Authenticate with Google Drive API
   - Use or generate token for future access

2. **Video Processing**
   - Download videos from Google Drive
   - Store temporarily in `temp_videos/`
   - Process audio for transcription

3. **Transcription**
   - Send audio to transcription API
   - Receive and format transcription text

4. **Analysis**
   - Send transcription to analysis API
   - Generate criteria based on content

5. **Storage**
   - Save results to SQLite database
   - Include video URL, transcription, and criteria

6. **Cleanup**
   - Remove temporary files after processing
   - Auto-cleanup files older than 24 hours

## Error Handling

- Comprehensive logging of all operations
- Automatic cleanup of temporary files
- Transaction-based database operations
- API error handling and retries

## Maintenance

### Temporary Files
- Located in `temp_videos/` directory
- Automatically cleaned up after:
  - Successful processing
  - 24 hours (configurable)
  - Script errors

### Logs
- Detailed logging of all operations
- Error tracking and debugging information

## Security Considerations

- Store API keys securely
- Use environment variables for sensitive data
- Regular cleanup of temporary files
- Secure database connections

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

[Specify your license here]

## Support

For support and questions, please [create an issue](your-issue-tracker-url) in the repository.