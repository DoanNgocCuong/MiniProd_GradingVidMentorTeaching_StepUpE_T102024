### update workflow3_fullaccess.py (xử lý với việc folder, file ko public mà cần quyền) với: 
```bash
SCOPES = [
    'https://www.googleapis.com/auth/drive',  # Full access
    'https://www.googleapis.com/auth/drive.file',  # Access to files created/opened by the app
    'https://www.googleapis.com/auth/drive.readonly'  # Read-only access to files
]
```
và 
Thay thế gdown.download bằng phương thức download_file mới sử dụng Google Drive API trực tiếp